"""
liveness_detection.py
Anti-spoofing: detects blinks, head turns, smiles.
Issues random challenges to the user to prove they are real.
Uses MediaPipe Face Mesh blendshapes and landmark distances.
"""

import cv2
import numpy as np
import mediapipe as mp
import random
import time

mp_face_mesh = mp.solutions.face_mesh

# Eye landmark indices for EAR (Eye Aspect Ratio)
LEFT_EYE  = [33, 160, 158, 133, 153, 144]
RIGHT_EYE = [362, 385, 387, 263, 373, 380]

# Mouth landmarks for smile/open detection
MOUTH_LANDMARKS = [61, 291, 13, 14]

CHALLENGES = [
    "blink_twice",
    "turn_left",
    "turn_right",
    "look_up",
    "smile",
]

def _eye_aspect_ratio(landmarks, eye_indices, w, h):
    """
    EAR = (vertical distance sum) / (2 * horizontal distance)
    When EAR < 0.2, the eye is closed (blink).
    """
    pts = [(int(landmarks.landmark[i].x * w),
            int(landmarks.landmark[i].y * h))
           for i in eye_indices]

    # Vertical
    v1 = np.linalg.norm(np.array(pts[1]) - np.array(pts[5]))
    v2 = np.linalg.norm(np.array(pts[2]) - np.array(pts[4]))
    # Horizontal
    h1 = np.linalg.norm(np.array(pts[0]) - np.array(pts[3]))

    ear = (v1 + v2) / (2.0 * h1 + 1e-6)
    return ear

class LivenessChecker:
    """
    Manages the liveness challenge flow.
    Call `get_challenge()` to get the current challenge string.
    Call `update(frame)` every frame; returns True when challenge is passed.
    """

    def __init__(self):
        self.face_mesh = mp_face_mesh.FaceMesh(
            max_num_faces=1,
            refine_landmarks=True,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )
        self.challenge = random.choice(CHALLENGES)
        self.challenge_start = time.time()
        self.blink_count = 0
        self._last_ear = 1.0
        self.passed = False

    def get_challenge(self) -> str:
        """Return human-readable challenge instruction."""
        messages = {
            "blink_twice": "Please blink twice",
            "turn_left":   "Turn your head LEFT",
            "turn_right":  "Turn your head RIGHT",
            "look_up":     "Look UP",
            "smile":       "Please SMILE",
        }
        return messages.get(self.challenge, "Follow the instruction")

    def update(self, frame: np.ndarray) -> bool:
        """
        Process a frame and return True if the current challenge is satisfied.
        """
        if self.passed:
            return True

        h, w = frame.shape[:2]
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.face_mesh.process(rgb)

        if not results.multi_face_landmarks:
            return False

        lm = results.multi_face_landmarks[0]

        if self.challenge == "blink_twice":
            ear = (_eye_aspect_ratio(lm, LEFT_EYE, w, h) +
                   _eye_aspect_ratio(lm, RIGHT_EYE, w, h)) / 2.0
            # Detect blink transition: open -> closed -> open
            if self._last_ear > 0.2 and ear < 0.2:
                self.blink_count += 1
            self._last_ear = ear
            if self.blink_count >= 2:
                self.passed = True

        elif self.challenge == "turn_left":
            # Nose tip x < 0.4 means head turned left (from user's perspective)
            nose_x = lm.landmark[1].x
            if nose_x < 0.40:
                self.passed = True

        elif self.challenge == "turn_right":
            nose_x = lm.landmark[1].x
            if nose_x > 0.60:
                self.passed = True

        elif self.challenge == "look_up":
            # Nose tip y < 0.4 means looking up
            nose_y = lm.landmark[1].y
            if nose_y < 0.40:
                self.passed = True

        elif self.challenge == "smile":
            # Mouth width relative to face width
            mouth_left  = np.array([lm.landmark[61].x,  lm.landmark[61].y])
            mouth_right = np.array([lm.landmark[291].x, lm.landmark[291].y])
            mouth_width = np.linalg.norm(mouth_right - mouth_left)
            # Face width (ear to ear roughly)
            face_left  = np.array([lm.landmark[234].x, lm.landmark[234].y])
            face_right = np.array([lm.landmark[454].x, lm.landmark[454].y])
            face_width = np.linalg.norm(face_right - face_left)
            smile_ratio = mouth_width / (face_width + 1e-6)
            if smile_ratio > 0.45:
                self.passed = True

        return self.passed

    def reset_challenge(self):
        """Pick a new random challenge."""
        self.challenge = random.choice(CHALLENGES)
        self.blink_count = 0
        self._last_ear = 1.0
        self.passed = False
        self.challenge_start = time.time()
