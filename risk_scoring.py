"""
risk_scoring.py
Central rule-based + AI risk engine.
Combines all signals to produce:
- Risk score (0-100)
- Cheating probability (0-100%)
"""

import numpy as np
import time


class RiskScorer:
    """
    Aggregates evidence from all sub-systems into a single risk score.
    Uses rule-based penalties + AI model outputs.
    """

    # How much each event adds to the risk score
    RISK_WEIGHTS = {
        "phone_detected":        25,
        "extra_person":          20,
        "talking":               15,
        "looking_away_long":     10,
        "identity_low":          20,
        "anomaly_detected":      15,
        "head_turned":            8,
        "left_frame":            18,
        "mouth_covered":         12,
        "object_detected":        8,
        "keystroke_mismatch":    10,
        "mouse_mismatch":         8,
    }

    def __init__(self):
        self.risk_score        = 0.0
        self.cheating_prob     = 0.0
        self._away_start       = None
        self._away_threshold   = 5.0   # seconds before counting as "long"

    def compute(self,
                behaviour_pred: dict,
                anomaly_result: dict,
                identity_conf: float,
                phone_detected: bool,
                person_count: int,
                gaze_dir: str,
                mouth_open: float,
                in_frame: bool,
                mouth_covered: bool,
                object_count: int,
                keystroke_sim: float,
                mouse_sim: float,
                away_time: float) -> dict:
        """
        Compute the current risk score and cheating probability.
        Returns a dict with all risk details.
        """
        penalties = {}
        total = 0.0

        if phone_detected:
            penalties["phone_detected"] = self.RISK_WEIGHTS["phone_detected"]

        if person_count > 1:
            penalties["extra_person"] = self.RISK_WEIGHTS["extra_person"] * (person_count - 1)

        if mouth_open > 0.3:  # talking
            penalties["talking"] = self.RISK_WEIGHTS["talking"]

        if away_time > self._away_threshold:
            penalties["looking_away_long"] = self.RISK_WEIGHTS["looking_away_long"]

        if identity_conf < 0.5:
            penalties["identity_low"] = int(self.RISK_WEIGHTS["identity_low"] * (1.0 - identity_conf * 2))

        if anomaly_result.get("is_anomaly", False):
            penalties["anomaly_detected"] = int(
                self.RISK_WEIGHTS["anomaly_detected"] * anomaly_result.get("anomaly_magnitude", 0.5)
            )

        if not in_frame:
            penalties["left_frame"] = self.RISK_WEIGHTS["left_frame"]

        if mouth_covered:
            penalties["mouth_covered"] = self.RISK_WEIGHTS["mouth_covered"]

        if object_count > 0:
            penalties["object_detected"] = self.RISK_WEIGHTS["object_detected"] * min(object_count, 3)

        if keystroke_sim < 0.4:
            penalties["keystroke_mismatch"] = self.RISK_WEIGHTS["keystroke_mismatch"]

        if mouse_sim < 0.4:
            penalties["mouse_mismatch"] = self.RISK_WEIGHTS["mouse_mismatch"]

        # Add behaviour model contribution
        cheat_prob_from_model = behaviour_pred.get("prob_cheating", 0.0)
        model_penalty = cheat_prob_from_model * 30  # up to 30 extra points

        total = sum(penalties.values()) + model_penalty

        # Clamp to 0-100
        self.risk_score = float(min(total, 100.0))

        # Cheating probability: weighted combination of risk score and model output
        self.cheating_prob = float(min(
            0.7 * (self.risk_score / 100.0) + 0.3 * cheat_prob_from_model,
            1.0
        ) * 100.0)

        return {
            "risk_score":       self.risk_score,
            "cheating_prob":    self.cheating_prob,
            "penalties":        penalties,
            "model_cheating":   cheat_prob_from_model,
        }
