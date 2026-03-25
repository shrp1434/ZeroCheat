"""
pose_analysis.py
Uses MediaPipe Pose to detect shoulder movement, hand movement,
body leaving frame, and general body language anomalies.
"""

import cv2
import numpy as np
import mediapipe as mp
import time

mp_pose = mp.solutions.pose

# Key landmark indices
LEFT_SHOULDER  = 11
RIGHT_SHOULDER = 12
LEFT_WRIST     = 15
RIGHT_WRIST    = 16
NOSE           = 0


class PoseAnalyser:
    def __init__(self):
        self.pose = mp_pose.Pose(
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )
        self._prev_shoulder_pos = None
        self._prev_wrist_pos    = None
        self.shoulder_movement  = 0.0
        self.hand_movement      = 0.0
        self.in_frame           = True
        self.mouth_covered      = False

    def update(self, frame: np.ndarray) -> dict:
        """
        Analyse pose in frame.
        Returns a dict with movement metrics.
        """
        h, w = frame.shape[:2]
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.pose.process(rgb)

        if not results.pose_landmarks:
            self.in_frame = False
            return {
                "shoulder_movement": self.shoulder_movement,
                "hand_movement":     self.hand_movement,
                "in_frame":          False,
                "mouth_covered":     False,
            }

        self.in_frame = True
        lm = results.pose_landmarks.landmark

        def pt(idx):
            return np.array([lm[idx].x, lm[idx].y])

        # Shoulder movement (average of both shoulders)
        shoulder_pos = (pt(LEFT_SHOULDER) + pt(RIGHT_SHOULDER)) / 2.0
        if self._prev_shoulder_pos is not None:
            self.shoulder_movement = float(
                np.linalg.norm(shoulder_pos - self._prev_shoulder_pos)
            )
        self._prev_shoulder_pos = shoulder_pos

        # Wrist/hand movement
        # Check if wrist landmarks are visible
        left_vis  = lm[LEFT_WRIST].visibility
        right_vis = lm[RIGHT_WRIST].visibility

        wrist_pos = None
        if left_vis > 0.5 and right_vis > 0.5:
            wrist_pos = (pt(LEFT_WRIST) + pt(RIGHT_WRIST)) / 2.0
        elif left_vis > 0.5:
            wrist_pos = pt(LEFT_WRIST)
        elif right_vis > 0.5:
            wrist_pos = pt(RIGHT_WRIST)

        if wrist_pos is not None and self._prev_wrist_pos is not None:
            self.hand_movement = float(
                np.linalg.norm(wrist_pos - self._prev_wrist_pos)
            )
        if wrist_pos is not None:
            self._prev_wrist_pos = wrist_pos

        # Mouth covered: if a wrist is very close to the nose landmark
        nose_pos = pt(NOSE)
        mouth_covered = False
        if left_vis > 0.5 and np.linalg.norm(pt(LEFT_WRIST) - nose_pos) < 0.1:
            mouth_covered = True
        if right_vis > 0.5 and np.linalg.norm(pt(RIGHT_WRIST) - nose_pos) < 0.1:
            mouth_covered = True
        self.mouth_covered = mouth_covered

        return {
            "shoulder_movement": self.shoulder_movement,
            "hand_movement":     self.hand_movement,
            "in_frame":          True,
            "mouth_covered":     mouth_covered,
        }
