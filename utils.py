"""
utils.py
Shared utility functions.
"""

import cv2
import os
import time
import numpy as np


SCREENSHOTS_DIR = "screenshots"
os.makedirs(SCREENSHOTS_DIR, exist_ok=True)


def save_screenshot(frame: np.ndarray, session_id: int) -> str:
    """Save a frame as a JPEG and return the file path."""
    filename = f"{SCREENSHOTS_DIR}/session_{session_id}_{int(time.time())}.jpg"
    cv2.imwrite(filename, frame)
    return filename


def frame_to_base64(frame: np.ndarray) -> str:
    """Convert a numpy frame to a base64 string for embedding in HTML."""
    import base64
    _, buffer = cv2.imencode(".jpg", frame)
    return base64.b64encode(buffer).decode("utf-8")


def clamp(value, min_val, max_val):
    return max(min_val, min(max_val, value))


def risk_to_color(risk: float) -> str:
    """Return a hex colour string based on risk level."""
    if risk < 30:
        return "#2ecc71"   # green
    elif risk < 60:
        return "#f39c12"   # orange
    else:
        return "#e74c3c"   # red
