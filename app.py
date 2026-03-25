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

    # ─── (Continuation of app.py) ────────────────────────────────────────────────

@app.route("/exam")
def exam():
    if "user_id" not in session:
        return redirect(url_for("login"))

    global exam_monitor
    user_id = session["user_id"]

    # Start a new exam session in the DB
    session_id = start_session(user_id)
    session["session_id"] = session_id

    # Start the AI monitoring engine
    exam_monitor = ExamMonitor(user_id, session_id, camera)
    exam_monitor.start()

    return render_template("exam.html",
                           username=session.get("username"),
                           session_id=session_id)


@app.route("/exam_status")
def exam_status():
    """AJAX endpoint: return current monitoring state as JSON."""
    if exam_monitor is None:
        return jsonify({"risk_score": 0, "cheating_prob": 0,
                        "identity_conf": 100, "alerts": []})
    state = dict(exam_monitor.current_state)
    state.pop("annotated_frame", None)   # can't JSON-serialise numpy array
    return jsonify(state)


@app.route("/end_exam")
def end_exam():
    global exam_monitor
    if exam_monitor:
        exam_monitor.stop()
        state = exam_monitor.current_state
        end_session(
            session.get("session_id", 0),
            state.get("risk_score", 0),
            state.get("cheating_prob", 0)
        )
        exam_monitor = None
    return redirect(url_for("reports"))


# ─── Dashboard ────────────────────────────────────────────────────────────────

@app.route("/dashboard")
def dashboard():
    sessions = get_all_sessions()
    return render_template("dashboard.html", sessions=sessions)


# ─── Logs ─────────────────────────────────────────────────────────────────────

@app.route("/logs")
def logs():
    all_sessions = get_all_sessions()
    selected_id  = request.args.get("session_id", type=int)

    if selected_id:
        events = get_events_for_session(selected_id)
    else:
        # Show all events from all sessions
        conn = get_connection()
        rows = conn.execute("SELECT * FROM events ORDER BY timestamp DESC LIMIT 200").fetchall()
        conn.close()
        events = [dict(r) for r in rows]

    return render_template("logs.html",
                           events=events,
                           all_sessions=all_sessions,
                           selected_session_id=selected_id)


@app.route("/screenshot/<int:event_id>")
def screenshot(event_id):
    """Serve a screenshot image for an event."""
    conn = get_connection()
    row = conn.execute("SELECT screenshot_path FROM events WHERE id=?", (event_id,)).fetchone()
    conn.close()
    if row and row["screenshot_path"] and os.path.exists(row["screenshot_path"]):
        return send_file(row["screenshot_path"], mimetype="image/jpeg")
    return "Screenshot not found", 404


# ─── Reports ──────────────────────────────────────────────────────────────────

@app.route("/reports")
def reports():
    sessions = get_all_sessions()
    return render_template("reports.html", sessions=sessions)


@app.route("/generate_report/<int:session_id>")
def generate_report_route(session_id):
    """Generate a PDF report and send it to the browser for download."""
    user_id = session.get("user_id", 1)
    pdf_path = generate_report(session_id, user_id)
    return send_file(pdf_path, as_attachment=True,
                     download_name=f"exam_report_session_{session_id}.pdf")


# ─── Admin ────────────────────────────────────────────────────────────────────

@app.route("/admin")
def admin():
    users = get_all_users()
    return render_template("admin.html", users=users)


@app.route("/admin/delete_user/<int:user_id>")
def delete_user(user_id):
    conn = get_connection()
    conn.execute("DELETE FROM users WHERE id=?",        (user_id,))
    conn.execute("DELETE FROM face_data WHERE user_id=?", (user_id,))
    conn.execute("DELETE FROM iris_data WHERE user_id=?", (user_id,))
    conn.commit()
    conn.close()
    flash("User deleted.", "success")
    return redirect(url_for("admin"))


@app.route("/admin/retrain_behaviour")
def retrain_behaviour():
    from behaviour_model import train_behaviour_model
    train_behaviour_model()
    flash("Behaviour model retrained successfully.", "success")
    return redirect(url_for("admin"))


@app.route("/admin/retrain_anomaly")
def retrain_anomaly():
    from anomaly_detection import train_anomaly_models
    train_anomaly_models()
    flash("Anomaly models retrained successfully.", "success")
    return redirect(url_for("admin"))


# ─── Logout ───────────────────────────────────────────────────────────────────

@app.route("/logout")
def logout():
    session.clear()
    flash("Logged out.", "success")
    return redirect(url_for("login"))


# ─── Main ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    camera.start()
    app.run(debug=False, host="0.0.0.0", port=5000, threaded=True)

    if "user_id" not in session:
        return redirect(url_for("login"))

    global exam_monitor
    user
