"""
face_recognition_module.py
Handles face registration and continuous verification.
Uses the face_recognition library (dlib underneath).
Stores 128-dimensional face encodings in SQLite as binary blobs.
"""

import face_recognition
import numpy as np
import pickle
import cv2
from database import get_connection

# How similar two faces must be to count as a match (lower = stricter)
FACE_MATCH_THRESHOLD = 0.5

def register_face(user_id: int, frame: np.ndarray) -> bool:
    """
    Detect a face in `frame` and save its encoding to the database.
    Returns True if a face was found and saved.
    """
    # face_recognition works with RGB, OpenCV uses BGR
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    encodings = face_recognition.face_encodings(rgb)

    if not encodings:
        print("[FaceRec] No face found during registration.")
        return False

    # Take the first (largest) face
    encoding = encodings[0]

    # Serialise the numpy array to bytes for SQLite storage
    blob = pickle.dumps(encoding)

    conn = get_connection()
    conn.execute(
        "INSERT INTO face_data (user_id, encoding) VALUES (?, ?)",
        (user_id, blob)
    )
    conn.commit()
    conn.close()
    print(f"[FaceRec] Face registered for user_id={user_id}.")
    return True

def load_face_encodings(user_id: int) -> list:
    """Load all stored face encodings for a user."""
    conn = get_connection()
    rows = conn.execute(
        "SELECT encoding FROM face_data WHERE user_id=?", (user_id,)
    ).fetchall()
    conn.close()
    return [pickle.loads(row["encoding"]) for row in rows]

def verify_face(user_id: int, frame: np.ndarray) -> float:
    """
    Compare the face in `frame` against stored encodings.
    Returns a confidence score from 0.0 (no match) to 1.0 (perfect match).
    """
    known_encodings = load_face_encodings(user_id)
    if not known_encodings:
        return 0.0

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(rgb)
    face_encodings = face_recognition.face_encodings(rgb, face_locations)

    if not face_encodings:
        return 0.0  # no face visible

    current_encoding = face_encodings[0]

    # Compute distances (lower = more similar)
    distances = face_recognition.face_distance(known_encodings, current_encoding)
    best_distance = min(distances)

    # Convert distance to a confidence score (1.0 = perfect)
    confidence = max(0.0, 1.0 - (best_distance / FACE_MATCH_THRESHOLD))
    return min(confidence, 1.0)

def detect_faces_in_frame(frame: np.ndarray) -> list:
    """Return list of face bounding boxes (top, right, bottom, left) in the frame."""
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    return face_recognition.face_locations(rgb)
