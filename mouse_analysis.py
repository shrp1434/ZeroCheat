"""
mouse_analysis.py
Captures mouse biometrics:
- Movement speed
- Acceleration
- Click intervals
- Movement patterns (straightness of paths)

Uses pynput for mouse event capture.
"""

import time
import threading
import numpy as np
import pickle
from pynput import mouse
from database import get_connection


class MouseAnalyser:
    def __init__(self):
        self._positions     = []    # (x, y, timestamp)
        self._click_times   = []    # timestamps of clicks
        self._lock          = threading.Lock()
        self._listener      = None

    def start(self):
        self._listener = mouse.Listener(
            on_move=self._on_move,
            on_click=self._on_click,
        )
        self._listener.daemon = True
        self._listener.start()

    def stop(self):
        if self._listener:
            self._listener.stop()

    def _on_move(self, x, y):
        with self._lock:
            self._positions.append((x, y, time.time()))
            # Keep only last 500 positions to save memory
            if len(self._positions) > 500:
                self._positions = self._positions[-500:]

    def _on_click(self, x, y, button, pressed):
        if pressed:
            with self._lock:
                self._click_times.append(time.time())

    def _compute_speeds(self) -> list:
        """Compute instantaneous speeds between consecutive points."""
        speeds = []
        pts = self._positions
        for i in range(1, len(pts)):
            dx = pts[i][0] - pts[i-1][0]
            dy = pts[i][1] - pts[i-1][1]
            dt = pts[i][2] - pts[i-1][2]
            if dt > 0:
                speed = np.sqrt(dx**2 + dy**2) / dt
                speeds.append(speed)
        return speeds

    def get_features(self) -> dict:
        with self._lock:
            positions = list(self._positions)
            clicks    = list(self._click_times)

        speeds = self._compute_speeds()

        avg_speed  = float(np.mean(speeds))       if speeds else 0.0
        std_speed  = float(np.std(speeds))        if speeds else 0.0
        max_speed  = float(np.max(speeds))        if speeds else 0.0

        # Acceleration: difference of consecutive speeds
        accels = [abs(speeds[i] - speeds[i-1]) for i in range(1, len(speeds))]
        avg_accel = float(np.mean(accels)) if accels else 0.0

        # Click interval
        click_intervals = [clicks[i] - clicks[i-1] for i in range(1, len(clicks))]
        avg_click = float(np.mean(click_intervals)) if click_intervals else 0.0

        return {
            "avg_speed":     avg_speed,
            "std_speed":     std_speed,
            "max_speed":     max_speed,
            "avg_accel":     avg_accel,
            "avg_click_interval": avg_click,
        }

    def save_profile(self, user_id: int):
        features = self.get_features()
        blob = pickle.dumps(features)
        conn = get_connection()
        conn.execute("""
            INSERT INTO mouse_data
            (user_id, avg_speed, avg_acceleration, click_interval, profile_blob)
            VALUES (?,?,?,?,?)
        """, (
            user_id,
            features["avg_speed"],
            features["avg_accel"],
            features["avg_click_interval"],
            blob,
        ))
        conn.commit()
        conn.close()

    def compare_to_profile(self, user_id: int) -> float:
        conn = get_connection()
        row = conn.execute(
            "SELECT profile_blob FROM mouse_data WHERE user_id=? ORDER BY id DESC LIMIT 1",
            (user_id,)
        ).fetchone()
        conn.close()

        if not row:
            return 0.5

        stored  = pickle.loads(row["profile_blob"])
        current = self.get_features()

        def norm_diff(a, b, scale):
            return abs(a - b) / (scale + 1e-6)

        diffs = [
            norm_diff(current["avg_speed"],  stored["avg_speed"],  200.0),
            norm_diff(current["avg_accel"],  stored["avg_accel"],  100.0),
            norm_diff(current["avg_click_interval"], stored["avg_click_interval"], 2.0),
        ]
        return max(0.0, 1.0 - float(np.mean(diffs)))
