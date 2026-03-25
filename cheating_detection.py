"""
cheating_detection.py
The central AI decision engine.
Orchestrates all sub-modules each frame/cycle.
Designed to be run in a background thread during the exam.
"""

import time
import threading
import numpy as np
import cv2
import os

from camera              import Camera
from face_recognition_module import verify_face
from iris_recognition_module import verify_iris
from liveness_detection  import LivenessChecker
from gaze_tracking       import GazeTracker
from head_pose           import HeadPoseEstimator
from pose_analysis       import PoseAnalyser
from object_detection    import ObjectDetector
from keystroke_analysis  import KeystrokeAnalyser
from mouse_analysis      import MouseAnalyser
from feature_extraction  import FeatureExtractor
from behaviour_model     import BehaviourClassifier
from anomaly_detection   import AnomalyDetector
from identity_model      import IdentityModel
from risk_scoring        import RiskScorer
from database            import insert_risk_score, insert_event, insert_behaviour_features
import utils


class ExamMonitor:
    """
    Main monitoring engine. Runs all AI subsystems together.
    Call start() to begin, stop() to end the exam session.
    Access current_state dict for real-time dashboard data.
    """

    def __init__(self, user_id: int, session_id: int, camera: Camera):
        self.user_id    = user_id
        self.session_id = session_id
        self.camera     = camera
        self.running    = False

        # Initialise all AI subsystems
        self.gaze_tracker  = GazeTracker()
        self.head_pose     = HeadPoseEstimator()
        self.pose_analyser = PoseAnalyser()
        self.obj_detector  = ObjectDetector()
        self.keystroke     = KeystrokeAnalyser()
        self.mouse         = MouseAnalyser()
        self.feature_ext   = FeatureExtractor(session_id)
        self.behaviour     = BehaviourClassifier()
        self.anomaly       = AnomalyDetector()
        self.identity      = IdentityModel()
        self.risk          = RiskScorer()

        # Blink tracking state
        self._blink_count  = 0
        self._blink_start  = time.time()

        # Current state (read by Flask dashboard)
        self.current_state = {
            "risk_score":       0.0,
            "cheating_prob":    0.0,
            "identity_conf":    1.0,
            "gaze_direction":   "center",
            "head_pitch":       0.0,
            "head_yaw":         0.0,
            "head_roll":        0.0,
            "phone_detected":   False,
            "person_count":     1,
            "behaviour_label":  "Normal",
            "alerts":           [],
            "annotated_frame":  None,
        }

        # Throttle YOLO (runs slower than face mesh)
        self._last_yolo = 0
        self.YOLO_INTERVAL = 2.0  # run YOLO every 2 seconds

    def start(self):
        """Start monitoring in a background thread."""
        self.keystroke.start()
        self.mouse.start()
        self.running = True
        self._thread = threading.Thread(target=self._monitor_loop, daemon=True)
        self._thread.start()
        print(f"[ExamMonitor] Started for user={self.user_id}, session={self.session_id}")

    def stop(self):
        self.running = False
        self.keystroke.stop()
        self.mouse.stop()
        print("[ExamMonitor] Stopped.")

    def _monitor_loop(self):
        """Main monitoring loop - processes every available frame."""
        while self.running:
            frame = self.camera.get_frame()
            if frame is None:
                time.sleep(0.05)
                continue

            now = time.time()
            alerts = []
            annotated = frame.copy()

            # --- Gaze Tracking ---
            gaze_dir = self.gaze_tracker.update(frame)
            away_time = self.gaze_tracker.get_away_time()

            # --- Head Pose ---
            pitch, yaw, roll = self.head_pose.update(frame)

            # --- Pose Analysis (body) ---
            pose_data = self.pose_analyser.update(frame)

            # --- YOLO Object Detection (every 2 seconds) ---
            if now - self._last_yolo >= self.YOLO_INTERVAL:
                obj_data = self.obj_detector.detect(frame)
                annotated = self.obj_detector.annotate_frame(annotated)
                self._last_yolo = now
            else:
                obj_data = {
                    "phone_detected": self.obj_detector.phone_detected,
                    "person_count":   self.obj_detector.person_count,
                    "object_count":   len(self.obj_detector.detected_objects),
                }

            # --- Face Verification ---
            face_score = verify_face(self.user_id, frame)

            # --- Iris Verification ---
            iris_score = verify_iris(self.user_id, frame)

            # --- Biometric Similarity ---
            keystroke_sim = self.keystroke.compare_to_profile(self.user_id)
            mouse_sim     = self.mouse.compare_to_profile(self.user_id)

            # --- Identity Confidence ---
            identity_conf = self.identity.compute_confidence(
                face_score, iris_score, keystroke_sim, mouse_sim
            )

            # --- Feature Vector ---
            ks_feats = self.keystroke.get_features()
            ms_feats = self.mouse.get_features()

            features = self.feature_ext.build_vector(
                gaze_dir     = gaze_dir,
                head         = (pitch, yaw, roll),
                blink_rate   = self._blink_count,
                mouth_open   = pose_data.get("shoulder_movement", 0),
                shoulder_mov = pose_data.get("shoulder_movement", 0),
                hand_mov     = pose_data.get("hand_movement", 0),
                phone_detected = obj_data["phone_detected"],
                person_count   = obj_data["person_count"],
                typing_speed   = ks_feats["typing_speed"],
                mouse_speed    = ms_feats["avg_speed"],
                away_time      = away_time,
                object_count   = obj_data["object_count"],
            )

            self.feature_ext.maybe_save(features)

            # --- ML Models ---
            vec = self.feature_ext.to_ml_array(features)
            behaviour_pred = self.behaviour.predict(vec)
            anomaly_result = self.anomaly.score(vec)

            # --- Risk Scoring ---
            risk_result = self.risk.compute(
                behaviour_pred = behaviour_pred,
                anomaly_result = anomaly_result,
                identity_conf  = identity_conf,
                phone_detected = obj_data["phone_detected"],
                person_count   = obj_data["person_count"],
                gaze_dir       = gaze_dir,
                mouth_open     = 0.0,
                in_frame       = pose_data.get("in_frame", True),
                mouth_covered  = pose_data.get("mouth_covered", False),
                object_count   = obj_data["object_count"],
                keystroke_sim  = keystroke_sim,
                mouse_sim      = mouse_sim,
                away_time      = away_time,
            )

            # Save risk score periodically
            insert_risk_score(
                self.session_id,
                risk_result["risk_score"],
                risk_result["cheating_prob"],
                identity_conf
            )

            # --- Alert Generation ---
            if obj_data["phone_detected"]:
                alerts.append("⚠️ Phone detected!")
                insert_event(self.session_id, "phone_detected", "HIGH",
                             "Mobile phone detected in frame",
                             utils.save_screenshot(frame, self.session_id))

            if obj_data["person_count"] > 1:
                alerts.append(f"⚠️ {obj_data['person_count']} people detected!")
                insert_event(self.session_id, "extra_person", "HIGH",
                             f"Additional person detected (count={obj_data['person_count']})")

            if not pose_data.get("in_frame", True):
                alerts.append("⚠️ Student left frame!")
                insert_event(self.session_id, "left_frame", "HIGH", "Student left camera frame")

            if identity_conf < 0.4:
                alerts.append("⚠️ Identity not confirmed!")
                insert_event(self.session_id, "identity_low", "HIGH",
                             f"Identity confidence dropped to {identity_conf:.2f}")

            if away_time > 10:
                alerts.append(f"⚠️ Looking away for {away_time:.0f}s")

            if anomaly_result["is_anomaly"]:
                alerts.append("⚠️ Unusual behaviour detected")
                insert_event(self.session_id, "anomaly", "MEDIUM",
                             f"Anomaly magnitude: {anomaly_result['anomaly_magnitude']:.2f}")

            # --- Update shared state (thread-safe with dict assignment) ---
            self.current_state = {
                "risk_score":       risk_result["risk_score"],
                "cheating_prob":    risk_result["cheating_prob"],
                "identity_conf":    identity_conf * 100,
                "gaze_direction":   gaze_dir,
                "head_pitch":       round(pitch, 1),
                "head_yaw":         round(yaw, 1),
                "head_roll":        round(roll, 1),
                "phone_detected":   obj_data["phone_detected"],
                "person_count":     obj_data["person_count"],
                "behaviour_label":  behaviour_pred["label"],
                "alerts":           alerts[-5:],  # keep last 5 alerts
                "annotated_frame":  annotated,
                "face_score":       round(face_score * 100, 1),
                "keystroke_sim":    round(keystroke_sim * 100, 1),
                "mouse_sim":        round(mouse_sim * 100, 1),
            }

            time.sleep(0.1)   # ~10 fps processing rate
