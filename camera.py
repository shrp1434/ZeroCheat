"""
camera.py
Manages the webcam connection.
Provides frames to all other modules.
Thread-safe frame reading with a background thread.
"""

import cv2
import threading
import time

class Camera:
    def __init__(self, camera_index=0):
        self.index = camera_index
        self.cap = None
        self.frame = None
        self.running = False
        self._lock = threading.Lock()

    def start(self):
        """Open the webcam and start reading frames in a background thread."""
        self.cap = cv2.VideoCapture(self.index)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        self.running = True
        self._thread = threading.Thread(target=self._capture_loop, daemon=True)
        self._thread.start()
        print("[Camera] Started.")

    def _capture_loop(self):
        """Background loop that constantly reads the latest frame."""
        while self.running:
            ret, frame = self.cap.read()
            if ret:
                with self._lock:
                    self.frame = frame  # always keep the most recent frame
            time.sleep(0.01)  # ~100 fps max read rate

    def get_frame(self):
        """Return the most recent webcam frame (thread-safe)."""
        with self._lock:
            if self.frame is None:
                return None
            return self.frame.copy()

    def capture_still(self):
        """Take a single still photo (used during registration)."""
        return self.get_frame()

    def stop(self):
        """Stop the camera."""
        self.running = False
        if self.cap:
            self.cap.release()
        print("[Camera] Stopped.")

    def get_jpeg(self):
        """Return the current frame as a JPEG bytes object for web streaming."""
        frame = self.get_frame()
        if frame is None:
            return None
        _, jpeg = cv2.imencode(".jpg", frame)
        return jpeg.tobytes()
