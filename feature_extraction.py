"""
feature_extraction.py
Aggregates signals from all sub-systems into a single feature vector.
Saves features to the database every N seconds.
"""

import numpy as np
import time
from database import insert_behaviour_features

FEATURE_INTERVAL = 3  # seconds between feature saves


class FeatureExtractor:
    def __init__(self, session_id: int):
        self.session_id   = session_id
        self._last_save   = time.time()

    def build_vector(self,
                     gaze_dir: str,
                     head: tuple,
                     blink_rate: float,
                     mouth_open: float,
                     shoulder_mov: float,
                     hand_mov: float,
                     phone_detected: bool,
                     person_count: int,
                     typing_speed: float,
                     mouse_speed: float,
                     away_time: float,
                     object_count: int) -> dict:
        """
        Combine all sensor readings into one flat feature dictionary.
        """
        pitch, yaw, roll = head

        # Encode gaze direction as number for ML models
        gaze_map = {"center": 0, "left": 1, "right": 2, "up": 3, "down": 4, "unknown": -1}

        features = {
            "gaze_direction":   gaze_dir,
            "gaze_num":         gaze_map.get(gaze_dir, -1),
            "head_pitch":       float(pitch),
            "head_yaw":         float(yaw),
            "head_roll":        float(roll),
            "blink_rate":       float(blink_rate),
            "mouth_open_freq":  float(mouth_open),
            "shoulder_movement": float(shoulder_mov),
            "hand_movement":    float(hand_mov),
            "phone_detected":   int(phone_detected),
            "person_count":     int(person_count),
            "typing_speed":     float(typing_speed),
            "mouse_speed":      float(mouse_speed),
            "time_looking_away": float(away_time),
            "object_count":     int(object_count),
        }
        return features

    def to_ml_array(self, features: dict) -> np.ndarray:
        """Return numpy array of numeric features for ML models."""
        keys = [
            "gaze_num", "head_pitch", "head_yaw", "head_roll",
            "blink_rate", "mouth_open_freq", "shoulder_movement",
            "hand_movement", "phone_detected", "person_count",
            "typing_speed", "mouse_speed", "time_looking_away",
            "object_count",
        ]
        return np.array([features.get(k, 0.0) for k in keys], dtype=np.float32)

    def maybe_save(self, features: dict):
        """Save to DB if enough time has elapsed since last save."""
        now = time.time()
        if now - self._last_save >= FEATURE_INTERVAL:
            insert_behaviour_features(self.session_id, features)
            self._last_save = now
