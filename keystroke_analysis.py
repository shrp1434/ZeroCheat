"""
keystroke_analysis.py
Captures keystroke dynamics:
- Key hold time (how long a key is pressed)
- Flight time (time between key releases and next key press)
- Typing speed (characters per minute)
- Error rate (backspace usage)

Uses pynput to listen to keyboard events in the background.
Builds a biometric profile and compares live typing to the profile.
"""

import time
import threading
import numpy as np
import pickle
from pynput import keyboard
from database import get_connection


class KeystrokeAnalyser:
    def __init__(self):
        self._press_times   = {}    # key -> press timestamp
        self._release_times = {}    # key -> release timestamp
        self.hold_times     = []    # list of hold durations
        self.flight_times   = []    # list of flight durations
        self.key_count      = 0
        self.error_count    = 0
        self._last_release  = None
        self._start_time    = time.time()
        self._lock          = threading.Lock()
        self._listener      = None

    def start(self):
        """Start the background keyboard listener."""
        self._listener = keyboard.Listener(
            on_press=self._on_press,
            on_release=self._on_release
        )
        self._listener.daemon = True
        self._listener.start()

    def stop(self):
        if self._listener:
            self._listener.stop()

    def _on_press(self, key):
        t = time.time()
        key_str = str(key)
        with self._lock:
            self._press_times[key_str] = t
            self.key_count += 1
            # Track errors (backspace)
            if key == keyboard.Key.backspace:
                self.error_count += 1
            # Flight time: time from last release to this press
            if self._last_release is not None:
                flight = t - self._last_release
                if 0 < flight < 2.0:  # ignore long pauses
                    self.flight_times.append(flight)

    def _on_release(self, key):
        t = time.time()
        key_str = str(key)
        with self._lock:
            if key_str in self._press_times:
                hold = t - self._press_times[key_str]
                if 0 < hold < 1.0:  # sanity check
                    self.hold_times.append(hold)
            self._last_release = t

    def get_features(self) -> dict:
        """Return current typing feature statistics."""
        with self._lock:
            elapsed = time.time() - self._start_time
            typing_speed = (self.key_count / elapsed * 60) if elapsed > 0 else 0
            error_rate   = (self.error_count / max(self.key_count, 1))

            avg_hold   = float(np.mean(self.hold_times))   if self.hold_times   else 0.0
            avg_flight = float(np.mean(self.flight_times)) if self.flight_times else 0.0
            std_hold   = float(np.std(self.hold_times))    if self.hold_times   else 0.0

        return {
            "avg_hold_time":  avg_hold,
            "avg_flight_time": avg_flight,
            "std_hold_time":   std_hold,
            "typing_speed":    typing_speed,
            "error_rate":      error_rate,
            "key_count":       self.key_count,
        }

    def save_profile(self, user_id: int):
        """Save the current keystroke profile to the database."""
        features = self.get_features()
        profile_blob = pickle.dumps(features)
        conn = get_connection()
        conn.execute("""
            INSERT INTO keystroke_data
            (user_id, avg_hold_time, avg_flight_time, typing_speed, error_rate, profile_blob)
            VALUES (?,?,?,?,?,?)
        """, (
            user_id,
            features["avg_hold_time"],
            features["avg_flight_time"],
            features["typing_speed"],
            features["error_rate"],
            profile_blob,
        ))
        conn.commit()
        conn.close()
        print(f"[Keystroke] Profile saved for user_id={user_id}.")

    def compare_to_profile(self, user_id: int) -> float:
        """
        Compare live typing to stored profile.
        Returns similarity score 0.0 to 1.0.
        """
        conn = get_connection()
        row = conn.execute(
            "SELECT profile_blob FROM keystroke_data WHERE user_id=? ORDER BY id DESC LIMIT 1",
            (user_id,)
        ).fetchone()
        conn.close()

        if not row:
            return 0.5  # no baseline, neutral

        stored = pickle.loads(row["profile_blob"])
        current = self.get_features()

        # Compare 3 key metrics using normalised difference
        def norm_diff(a, b, scale):
            return abs(a - b) / (scale + 1e-6)

        diffs = [
            norm_diff(current["avg_hold_time"],   stored["avg_hold_time"],   0.1),
            norm_diff(current["avg_flight_time"], stored["avg_flight_time"], 0.2),
            norm_diff(current["typing_speed"],    stored["typing_speed"],    30.0),
        ]
        avg_diff = float(np.mean(diffs))
        return max(0.0, 1.0 - avg_diff)

    def reset(self):
        """Clear accumulated data (call at exam start)."""
        with self._lock:
            self.hold_times   = []
            self.flight_times = []
            self.key_count    = 0
            self.error_count  = 0
            self._start_time  = time.time()
