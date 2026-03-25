"""
gaze_tracking.py
Estimates gaze direction (left / right / up / down / center)
using the position of the iris centre relative to the eye socket.
"""

import cv2
import numpy as np
import mediapipe as mp

mp_face_mesh = mp.solutions.face_mesh

# Eye corner landmarks
LEFT_EYE_CORNERS  = [33, 133]   # inner, outer
RIGHT_EYE_CORNERS = [362, 263]

# Iris centre landmarks (from refine_landmarks=True)
LEFT_IRIS_CENTER  = 468
RIGHT_IRIS_CENTER = 473

# Upper and lower eyelid landmarks
LEFT_EYE_TOP    = 159
LEFT_EYE_BOTTOM = 145
RIGHT_EYE_TOP   = 386
RIGHT_EYE_BOTTOM = 374


class GazeTracker:
    def __init__(self):
        self.face_mesh = mp_face_mesh.FaceMesh(
            max_num_faces=1,
            refine_landmarks=True,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )
        self.gaze_direction = "center"
        self.looking_away_start = None
        self.total_away_time = 0.0

    def _get_gaze_ratio(self, lm, eye_corners, iris_idx, top_idx, bottom_idx, w, h):
        """
        Horizontal ratio: 0 = far left, 1 = far right, 0.5 = center
        Vertical ratio:   0 = far up,   1 = far down,  0.5 = center
        """
        inner  = np.array([lm.landmark[eye_corners[0]].x * w,
                            lm.landmark[eye_corners[0]].y * h])
        outer  = np.array([lm.landmark[eye_corners[1]].x * w,
                            lm.landmark[eye_corners[1]].y * h])
        iris   = np.array([lm.landmark[iris_idx].x * w,
                            lm.landmark[iris_idx].y * h])
        top    = np.array([lm.landmark[top_idx].x * w,
                            lm.landmark[top_idx].y * h])
        bottom = np.array([lm.landmark[bottom_idx].x * w,
                            lm.landmark[bottom_idx].y * h])

        eye_width   = np.linalg.norm(outer - inner) + 1e-6
        eye_height  = np.linalg.norm(bottom - top) + 1e-6

        h_ratio = np.dot(iris - inner, outer - inner) / (eye_width ** 2)
        v_ratio = np.dot(iris - top,   bottom - top)  / (eye_height ** 2)
        return h_ratio, v_ratio

    def update(self, frame: np.ndarray) -> str:
        """
        Process a frame and return gaze direction string.
        Also accumulates time-looking-away.
        """
        import time
        h, w = frame.shape[:2]
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.face_mesh.process(rgb)

        if not results.multi_face_landmarks:
            self.gaze_direction = "unknown"
            return "unknown"

        lm = results.multi_face_landmarks[0]

        lh, lv = self._get_gaze_ratio(lm, LEFT_EYE_CORNERS,  LEFT_IRIS_CENTER,
                                       LEFT_EYE_TOP,  LEFT_EYE_BOTTOM,  w, h)
        rh, rv = self._get_gaze_ratio(lm, RIGHT_EYE_CORNERS, RIGHT_IRIS_CENTER,
                                       RIGHT_EYE_TOP, RIGHT_EYE_BOTTOM, w, h)

        avg_h = (lh + rh) / 2.0
        avg_v = (lv + rv) / 2.0

        # Thresholds determined empirically
        if avg_h < 0.35:
            direction = "left"
        elif avg_h > 0.65:
            direction = "right"
        elif avg_v < 0.35:
            direction = "up"
        elif avg_v > 0.65:
            direction = "down"
        else:
            direction = "center"

        self.gaze_direction = direction

        # Track away time
        if direction != "center":
            if self.looking_away_start is None:
                self.looking_away_start = time.time()
            else:
                self.total_away_time += time.time() - self.looking_away_start
                self.looking_away_start = time.time()
        else:
            self.looking_away_start = None

        return direction

    def get_away_time(self) -> float:
        return self.total_away_time

    def reset_away_time(self):
        self.total_away_time = 0.0
