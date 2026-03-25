"""
object_detection.py
Uses YOLOv8 (ultralytics) with the pre-trained COCO model.
Detects suspicious objects: phone, book, laptop, person, etc.
The model file (yolov8n.pt) downloads automatically on first run.
"""

import cv2
import numpy as np
from ultralytics import YOLO
import os

# Suspicious object class names (from COCO dataset)
SUSPICIOUS_CLASSES = {
    "cell phone":  "high",    # phone = very suspicious
    "book":        "medium",
    "laptop":      "high",
    "tv":          "medium",  # extra monitor
    "person":      "high",    # another person in room
    "keyboard":    "low",     # already at desk, less suspicious
    "mouse":       "low",
    "headphones":  "medium",
    "remote":      "low",
    "tablet":      "high",
}


class ObjectDetector:
    def __init__(self, model_path: str = "yolov8n.pt", confidence: float = 0.4):
        """
        Load YOLOv8 nano model.
        yolov8n.pt downloads automatically from ultralytics servers on first use.
        """
        print("[YOLO] Loading YOLOv8 model...")
        self.model = YOLO(model_path)
        self.confidence = confidence
        self.detected_objects = []
        self.phone_detected = False
        self.person_count   = 0
        print("[YOLO] Model loaded.")

    def detect(self, frame: np.ndarray) -> dict:
        """
        Run YOLO detection on a frame.
        Returns dict with detected objects and risk flags.
        """
        results = self.model(frame, conf=self.confidence, verbose=False)

        detected = []
        phone    = False
        persons  = 0

        for result in results:
            for box in result.boxes:
                class_id   = int(box.cls[0])
                class_name = result.names[class_id].lower()
                confidence = float(box.conf[0])

                if class_name in SUSPICIOUS_CLASSES:
                    detected.append({
                        "class":      class_name,
                        "confidence": confidence,
                        "severity":   SUSPICIOUS_CLASSES[class_name],
                        "box":        box.xyxy[0].tolist(),
                    })

                if class_name == "cell phone":
                    phone = True
                if class_name == "person":
                    persons += 1

        self.detected_objects = detected
        self.phone_detected   = phone
        self.person_count     = persons

        return {
            "objects":        detected,
            "phone_detected": phone,
            "person_count":   persons,
            "object_count":   len(detected),
        }

    def annotate_frame(self, frame: np.ndarray) -> np.ndarray:
        """Draw bounding boxes on the frame for detected suspicious objects."""
        annotated = frame.copy()
        for obj in self.detected_objects:
            x1, y1, x2, y2 = [int(v) for v in obj["box"]]
            color = (0, 0, 255) if obj["severity"] == "high" else (0, 165, 255)
            cv2.rectangle(annotated, (x1, y1), (x2, y2), color, 2)
            label = f"{obj['class']} {obj['confidence']:.2f}"
            cv2.putText(annotated, label, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
        return annotated
