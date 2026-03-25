"""
app.py
Flask web application.
Routes: register, login, liveness, exam, dashboard, logs, reports, admin.
Streams the live webcam feed as MJPEG to the browser.
"""

import cv2
import io
import os
import time
import threading
import json
import numpy as np
from flask import (
    Flask, render_template, request, redirect,
    url_for, session, jsonify, Response, send_file, flash
)

from camera              import Camera
from cheating_detection  import ExamMonitor
from face_recognition_module import register_face, verify_face
from iris_recognition_module import register_iris
from liveness_detection  import LivenessChecker
from keystroke_analysis  import KeystrokeAnalyser
from mouse_analysis      import MouseAnalyser
from report_generator    import generate_report
from database            import (
    init_db, insert_user, get_user_by_username,
    get_all_users, start_session, end_session,
    get_all_sessions, get_events_for_session,
    get_risk_scores_for_session, get_connection
)
import utils

# ─── App Setup ──────────────────────────────────────────────────────────────
app = Flask(__name__)
app.secret_key = "exam_monitor_secret_key_change_in_production"

# Global objects (shared across requests)
camera       = Camera()
liveness     = None   # set during liveness check
exam_monitor = None   # set during exam

# Initialise DB on startup
init_db()

# ─── Video Streaming ─────────────────────────────────────────────────────────

def gen_frames(annotated=False):
    """Generator that yields MJPEG frames for the browser."""
    while True:
        if annotated and exam_monitor is not None:
            frame = exam_monitor.current_state.get("annotated_frame")
        else:
            frame = camera.get_frame()

        if frame is None:
            time.sleep(0.05)
            continue

        _, buffer = cv2.imencode(".jpg", frame, [cv2.IMWRITE_JPEG_QUALITY, 70])
        yield (b"--frame\r\n"
               b"Content-Type: image/jpeg\r\n\r\n" +
               buffer.tobytes() + b"\r\n")
        time.sleep(0.04)  # ~25 fps


@app.route("/video_feed")
def video_feed():
    return Response(gen_frames(), mimetype="multipart/x-mixed-replace; boundary=frame")


@app.route("/video_feed_annotated")
def video_feed_annotated():
    return Response(gen_frames(annotated=True),
                    mimetype="multipart/x-mixed-replace; boundary=frame")


# ─── Home ─────────────────────────────────────────────────────────────────────

@app.route("/")
def index():
    if not camera.running:
        camera.start()
    return render_template("register.html")


# ─── Register ─────────────────────────────────────────────────────────────────

@app.route("/register", methods=["GET", "POST"])
def register():
    if not camera.running:
        camera.start()

    if request.method == "POST":
        username  = request.form.get("username", "").strip()
        full_name = request.form.get("full_name", "").strip()

        if not username:
            flash("Username is required.", "error")
            return render_template("register.html")

        if get_user_by_username(username):
            flash("Username already exists.", "error")
            return render_template("register.html")

        # Create user record
        user_id = insert_user(username, full_name)

        # Capture biometrics (3 frames for robustness)
        success_face = False
        for _ in range(5):
            frame = camera.capture_still()
            if frame is not None and register_face(user_id, frame):
                success_face = True
                break
            time.sleep(0.3)

        success_iris = False
        for _ in range(5):
            frame = camera.capture_still()
            if frame is not None and register_iris(user_id, frame):
                success_iris = True
                break
            time.sleep(0.3)

        flash(f"User '{username}' registered! Face: {success_face}, Iris: {success_iris}", "success")
        return redirect(url_for("login"))

    return render_template("register.html")


# ─── Login ─────────────────────────────────────────────────────────────────────

@app.route("/login", methods=["GET", "POST"])
def login():
    if not camera.running:
        camera.start()

    if request.method == "POST":
        username = request.form.get("username", "").strip()
        user     = get_user_by_username(username)

        if not user:
            flash("User not found.", "error")
            return render_template("login.html")

        # Verify face
        frame = camera.capture_still()
        if frame is None:
            flash("Camera error.", "error")
            return render_template("login.html")

        score = verify_face(user["id"], frame)
        if score < 0.4:
            flash(f"Face not recognised (score={score:.2f}). Try again.", "error")
            return render_template("login.html")

        # Store user in session
        session["user_id"]   = user["id"]
        session["username"]  = user["username"]
        session["full_name"] = user["full_name"]
        flash(f"Welcome, {user['full_name']}! Identity confirmed.", "success")
        return redirect(url_for("liveness_check"))

    return render_template("login.html")


# ─── Liveness ─────────────────────────────────────────────────────────────────

@app.route("/liveness")
def liveness_check():
    if "user_id" not in session:
        return redirect(url_for("login"))
    global liveness
    liveness = LivenessChecker()
    return render_template("liveness.html",
                           challenge=liveness.get_challenge())


@app.route("/liveness_status")
def liveness_status():
    """AJAX endpoint: check whether liveness challenge has been passed."""
    global liveness
    if liveness is None:
        return jsonify({"passed": False, "challenge": "No challenge active"})

    frame = camera.get_frame()
    if frame is not None:
        passed = liveness.update(frame)
    else:
        passed = False

    return jsonify({
        "passed":    passed,
        "challenge": liveness.get_challenge()
    })


@app.route("/liveness_passed")
def liveness_passed():
    return redirect(url_for("exam"))


# ─── Exam ─────────────────────────────────────────────────────────────────────

@app.route("/exam")
def exam():
    if "user_id" not in session:
        return redirect(url_for("login"))

    global exam_monitor
    user
