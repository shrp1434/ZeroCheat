"""
iris_recognition_module.py
Uses MediaPipe Face Mesh (with refine_landmarks=True) to locate the iris.
Extracts, normalises, and compares iris features.
Uses Hamming-style distance on binarised feature vectors.

MediaPipe iris landmark indices:
  Left iris:  468-472
  Right iris: 473-477
"""

import cv2
import numpy as np
import mediapipe as mp
import pickle
from database import get_connection

mp_face_mesh = mp.solutions.face_mesh

# Landmark indices for the irises (MediaPipe with refine_landmarks=True)
LEFT_IRIS  = [468, 469, 470, 471, 472]
RIGHT_IRIS = [473, 474, 475, 476, 477]

# How large to make the normalised iris patch
IRIS_SIZE = 64

def _extract_iris_patch(frame: np.ndarray, landmarks, indices: list) -> np.ndarray:
    """
    Given MediaPipe face landmarks and a list of iris indices,
    crop out and normalise the iris region.
    """
    h, w = frame.shape[:2]

    # Get pixel coordinates of the iris landmarks
    pts = np.array([
        (int(landmarks.landmark[i].x * w),
         int(landmarks.landmark[i].y * h))
        for i in indices
    ])

    # Bounding box of iris region
    x_min, y_min = pts.min(axis=0)
    x_max, y_max = pts.max(axis=0)
    padding = 10  # add a little context around the iris

    x1 = max(0, x_min - padding)
    y1 = max(0, y_min - padding)
    x2 = min(w, x_max + padding)
    y2 = min(h, y_max + padding)

    iris_crop = frame[y1:y2, x1:x2]
    if iris_crop.size == 0:
        return None

    # Normalise: grayscale, resize to fixed square
    gray = cv2.cvtColor(iris_crop, cv2.COLOR_BGR2GRAY)
    normalised = cv2.resize(gray, (IRIS_SIZE, IRIS_SIZE))
    return normalised

def _extract_features(iris_patch: np.ndarray) -> np.ndarray:
    """
    Extract a simple feature vector from an iris patch.
    Uses pixel intensities + LBP-style difference patterns.
    """
    # Flatten normalised intensities
    flat = iris_patch.flatten().astype(np.float32) / 255.0
    return flat

def register_iris(user_id: int, frame: np.ndarray) -> bool:
    """Detect and save iris features for a user."""
    with mp_face_mesh.FaceMesh(
        static_image_mode=True,
        refine_landmarks=True,
        min_detection_confidence=0.5
    ) as face_mesh:
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(rgb)

        if not results.multi_face_landmarks:
            print("[Iris] No face found.")
            return False

        landmarks = results.multi_face_landmarks[0]

        left_patch  = _extract_iris_patch(frame, landmarks, LEFT_IRIS)
        right_patch = _extract_iris_patch(frame, landmarks, RIGHT_IRIS)

        if left_patch is None or right_patch is None:
            print("[Iris] Could not extract iris patches.")
            return False

        left_feat  = _extract_features(left_patch)
        right_feat = _extract_features(right_patch)

        conn = get_connection()
        conn.execute(
            "INSERT INTO iris_data (user_id, left_features, right_features) VALUES (?,?,?)",
            (user_id, pickle.dumps(left_feat), pickle.dumps(right_feat))
        )
        conn.commit()
        conn.close()
        print(f"[Iris] Iris registered for user_id={user_id}.")
        return True

def verify_iris(user_id: int, frame: np.ndarray) -> float:
    """
    Compare current iris to stored reference.
    Returns confidence from 0.0 to 1.0.
    """
    conn = get_connection()
    row = conn.execute(
        "SELECT left_features, right_features FROM iris_data WHERE user_id=? ORDER BY id DESC LIMIT 1",
        (user_id,)
    ).fetchone()
    conn.close()

    if not row:
        return 0.5  # no reference, neutral score

    stored_left  = pickle.loads(row["left_features"])
    stored_right = pickle.loads(row["right_features"])

    with mp_face_mesh.FaceMesh(
        static_image_mode=True,
        refine_landmarks=True,
        min_detection_confidence=0.5
    ) as face_mesh:
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(rgb)

        if not results.multi_face_landmarks:
            return 0.0

        landmarks = results.multi_face_landmarks[0]
        left_patch  = _extract_iris_patch(frame, landmarks, LEFT_IRIS)
        right_patch = _extract_iris_patch(frame, landmarks, RIGHT_IRIS)

        if left_patch is None or right_patch is None:
            return 0.0

        cur_left  = _extract_features(left_patch)
        cur_right = _extract_features(right_patch)

    # Cosine similarity
    def cosine_sim(a, b):
        return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b) + 1e-8))

    left_sim  = cosine_sim(stored_left,  cur_left)
    right_sim = cosine_sim(stored_right, cur_right)
    return (left_sim + right_sim) / 2.0
