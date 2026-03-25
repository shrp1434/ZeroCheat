"""
anomaly_detection.py
Detects unusual behaviour patterns using unsupervised learning:
- Isolation Forest: detects outliers in feature space
- One-Class SVM: learned boundary around normal behaviour

These models are trained ONLY on normal behaviour data,
so any deviation from normal will be flagged.
"""

import numpy as np
import pickle
import os
from sklearn.ensemble import IsolationForest
from sklearn.svm import OneClassSVM
from sklearn.preprocessing import StandardScaler

ISO_PATH    = "isolation_forest.pkl"
OCSVM_PATH  = "one_class_svm.pkl"
AD_SCALER   = "anomaly_scaler.pkl"


def train_anomaly_models():
    """Train both anomaly models on synthetic normal behaviour."""
    print("[AnomalyDetection] Training anomaly models...")
    rng = np.random.default_rng(42)
    n = 1000

    # Generate only normal behaviour samples
    X = np.column_stack([
        rng.choice([0], n),               # gaze center
        rng.uniform(-5, 5, n),            # head_pitch
        rng.uniform(-10, 10, n),          # head_yaw
        rng.uniform(-5, 5, n),            # head_roll
        rng.uniform(10, 20, n),           # blink_rate
        rng.uniform(0, 0.1, n),           # mouth_open
        rng.uniform(0, 0.02, n),          # shoulder
        rng.uniform(0, 0.02, n),          # hand
        rng.choice([0], n),               # phone
        rng.choice([1], n),               # persons
        rng.uniform(30, 60, n),           # typing
        rng.uniform(50, 200, n),          # mouse
        rng.uniform(0, 5, n),             # away
        rng.choice([0], n),               # objects
    ])

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    iso   = IsolationForest(contamination=0.05, random_state=42)
    ocsvm = OneClassSVM(kernel="rbf", gamma="scale", nu=0.05)

    iso.fit(X_scaled)
    ocsvm.fit(X_scaled)

    with open(ISO_PATH,   "wb") as f: pickle.dump(iso,    f)
    with open(OCSVM_PATH, "wb") as f: pickle.dump(ocsvm,  f)
    with open(AD_SCALER,  "wb") as f: pickle.dump(scaler, f)
    print("[AnomalyDetection] Models saved.")
    return iso, ocsvm, scaler


def load_anomaly_models():
    if all(os.path.exists(p) for p in [ISO_PATH, OCSVM_PATH, AD_SCALER]):
        with open(ISO_PATH,   "rb") as f: iso    = pickle.load(f)
        with open(OCSVM_PATH, "rb") as f: ocsvm  = pickle.load(f)
        with open(AD_SCALER,  "rb") as f: scaler = pickle.load(f)
        print("[AnomalyDetection] Models loaded.")
        return iso, ocsvm, scaler
    return train_anomaly_models()


class AnomalyDetector:
    def __init__(self):
        self.iso, self.ocsvm, self.scaler = load_anomaly_models()

    def score(self, feature_vector: np.ndarray) -> dict:
        """
        Score a feature vector for anomalousness.
        Returns scores and an is_anomaly flag.
        Isolation Forest: -1=anomaly, 1=normal
        One-Class SVM:    -1=anomaly, 1=normal
        """
        X = feature_vector.reshape(1, -1)
        X_s = self.scaler.transform(X)

        iso_score  = float(self.iso.score_samples(X_s)[0])   # more negative = more anomalous
        iso_pred   = int(self.iso.predict(X_s)[0])
        ocsvm_pred = int(self.ocsvm.predict(X_s)[0])

        is_anomaly = (iso_pred == -1 or ocsvm_pred == -1)

        # Normalise isolation score to 0-1 (1=most anomalous)
        anomaly_magnitude = max(0.0, min(1.0, (-iso_score + 0.5) * 2))

        return {
            "iso_score":        iso_score,
            "is_anomaly":       is_anomaly,
            "anomaly_magnitude": anomaly_magnitude,
        }
