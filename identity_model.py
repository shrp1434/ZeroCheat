"""
identity_model.py
Combines face, iris, keystroke and mouse scores
into a single identity confidence score.
Uses weighted average with optional anomaly penalty.
"""

import numpy as np

# Weights for each biometric modality
WEIGHTS = {
    "face":      0.45,   # most reliable
    "iris":      0.25,
    "keystroke": 0.15,
    "mouse":     0.15,
}


class IdentityModel:
    def __init__(self):
        # Running average of confidence to smooth jitter
        self._history = []
        self.WINDOW   = 10   # number of samples to average

    def compute_confidence(self,
                           face_score: float,
                           iris_score: float,
                           keystroke_score: float,
                           mouse_score: float) -> float:
        """
        Compute weighted identity confidence 0.0 to 1.0.
        A score near 1.0 means the person is almost certainly the registered user.
        """
        raw = (
            WEIGHTS["face"]      * face_score +
            WEIGHTS["iris"]      * iris_score +
            WEIGHTS["keystroke"] * keystroke_score +
            WEIGHTS["mouse"]     * mouse_score
        )
        raw = float(np.clip(raw, 0.0, 1.0))

        # Smooth over a sliding window
        self._history.append(raw)
        if len(self._history) > self.WINDOW:
            self._history.pop(0)
        smoothed = float(np.mean(self._history))

        return smoothed

    def get_risk_from_identity(self, confidence: float) -> float:
        """
        Convert identity confidence to a risk contribution (0=no risk, 1=max risk).
        Low confidence = high identity risk.
        """
        return max(0.0, 1.0 - confidence)
