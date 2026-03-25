"""
head_pose.py
Estimates head pitch (nodding), yaw (turning), roll (tilting)
using the solvePnP algorithm with 6 key facial landmarks.
"""

import cv2
import numpy as np
import mediapipe as mp

mp_face_mesh = mp.solutions.face_mesh

# The 6 canonical 3D face model points (nose, chin, eyes, mouth corners)
MODEL_POINTS_3D = np.array([
    (0.0,    0.0,    0.0),      # Nose tip (landmark 1)
    (0.0,   -330.0, -65.0),     # Chin (landmark 152)
    (-225.0,  170.0, -135.0),   # Left eye corner (landmark 33)
    (225.0,   170.0, -135.0),   # Right eye corner (landmark 263)
    (-150.0, -150.0, -125.0),   # Left mouth corner (landmark 61)
    (150.0,  -150.0, -125.0),   # Right mouth corner (landmark 291)
], dtype=np.float64)

LANDMARK_IDS = [1, 152, 33, 263, 61, 291]


class HeadPoseEstimator:
    def __init__(self):
        self.face_mesh = mp_face_mesh.FaceMesh(
            max_num_faces=1,
            refine_landmarks=False,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )
        self.pitch = 0.0
        self.yaw   = 0.0
        self.roll  = 0.0

    def update(self, frame: np.ndarray):
        """
        Process frame, update pitch/yaw/roll.
        Returns (pitch, yaw, roll) in degrees.
        """
        h, w = frame.shape[:2]
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.face_mesh.process(rgb)

        if not results.multi_face_landmarks:
            return self.pitch, self.yaw, self.roll

        lm = results.multi_face_landmarks[0]

        # 2D image points from landmarks
        image_points = np.array([
            (lm.landmark[i].x * w, lm.landmark[i].y * h)
            for i in LANDMARK_IDS
        ], dtype=np.float64)

        # Camera intrinsics (approximate for typical webcam)
        focal_length = w
        cam_matrix = np.array([
            [focal_length, 0, w / 2],
            [0, focal_length, h / 2],
            [0, 0, 1]
        ], dtype=np.float64)

        dist_coeffs = np.zeros((4, 1))  # assuming no lens distortion

        success, rot_vec, trans_vec = cv2.solvePnP(
            MODEL_POINTS_3D, image_points, cam_matrix, dist_coeffs,
            flags=cv2.SOLVEPNP_ITERATIVE
        )

        if not success:
            return self.pitch, self.yaw, self.roll

        # Convert rotation vector to rotation matrix then to Euler angles
        rot_matrix, _ = cv2.Rodrigues(rot_vec)
        angles, _, _, _, _, _ = cv2.RQDecomp3x3(rot_matrix)

        self.pitch = angles[0]  # nodding up/down
        self.yaw   = angles[1]  # turning left/right
        self.roll  = angles[2]  # tilting

        return self.pitch, self.yaw, self.roll

    def is_looking_away(self) -> bool:
        """Return True if the head is turned significantly away from the screen."""
        return abs(self.yaw) > 20 or abs(self.pitch) > 15
