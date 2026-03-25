"""
behaviour_model.py
Trains and runs behaviour classification models:
- Random Forest
- SVM
- Logistic Regression

Classes: 0=Normal, 1=Suspicious, 2=Cheating

Since we start with no labelled data, the model initially uses
rule-based classification and improves as data accumulates.
Training data can be generated from historical sessions.
"""

import numpy as np
import pickle
import os
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

MODEL_PATH  = "behaviour_model.pkl"
SCALER_PATH = "behaviour_scaler.pkl"

# Class labels
NORMAL     = 0
SUSPICIOUS = 1
CHEATING   = 2


def generate_synthetic_training_data(n_samples=2000):
    """
    Generate synthetic labelled training data.
    In a real deployment, replace this with real labelled session data.

    Feature order:
    gaze_num, head_pitch, head_yaw, head_roll,
    blink_rate, mouth_open_freq, shoulder_movement, hand_movement,
    phone_detected, person_count, typing_speed, mouse_speed,
    time_looking_away, object_count
    """
    rng = np.random.default_rng(42)

    X, y = [], []

    for _ in range(n_samples // 3):
        # Normal student: looking forward, normal typing
        X.append([
            0,                           # gaze center
            rng.uniform(-5, 5),          # head pitch
            rng.uniform(-10, 10),        # head yaw
            rng.uniform(-5, 5),          # head roll
            rng.uniform(10, 20),         # blink rate (per minute)
            rng.uniform(0, 0.1),         # mouth open (not talking)
            rng.uniform(0, 0.02),        # shoulder movement
            rng.uniform(0, 0.02),        # hand movement
            0,                           # no phone
            1,                           # 1 person (just user)
            rng.uniform(30, 60),         # typing speed
            rng.uniform(50, 200),        # mouse speed
            rng.uniform(0, 5),           # looking away time (seconds)
            0,                           # no suspicious objects
        ])
        y.append(NORMAL)

    for _ in range(n_samples // 3):
        # Suspicious student: looking away, slow typing, slight head turn
        X.append([
            rng.choice([1, 2, 3, 4]),    # looking away
            rng.uniform(-15, 15),
            rng.uniform(-25, 25),
            rng.uniform(-10, 10),
            rng.uniform(5, 12),
            rng.uniform(0.1, 0.3),       # talking somewhat
            rng.uniform(0.02, 0.05),
            rng.uniform(0.02, 0.05),
            0,
            1,
            rng.uniform(0, 30),
            rng.uniform(0, 100),
            rng.uniform(10, 30),
            rng.choice([0, 1]),
        ])
        y.append(SUSPICIOUS)

    for _ in range(n_samples // 3):
        # Cheating: phone visible, another person, not looking at screen
        X.append([
            rng.choice([1, 2, 3, 4]),
            rng.uniform(-20, 20),
            rng.uniform(-35, 35),
            rng.uniform(-15, 15),
            rng.uniform(2, 8),
            rng.uniform(0.2, 0.8),       # talking a lot
            rng.uniform(0.05, 0.2),
            rng.uniform(0.05, 0.2),
            rng.choice([0, 1]),          # phone may be visible
            rng.choice([1, 2]),          # possibly another person
            rng.uniform(0, 20),
            rng.uniform(0, 50),
            rng.uniform(20, 60),
            rng.choice([1, 2, 3]),
        ])
        y.append(CHEATING)

    return np.array(X), np.array(y)


def train_behaviour_model():
    """Train the ensemble behaviour model and save to disk."""
    print("[BehaviourModel] Generating training data...")
    X, y = generate_synthetic_training_data(3000)

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.2, random_state=42
    )

    # Build an ensemble of 3 classifiers
    rf  = RandomForestClassifier(n_estimators=100, random_state=42)
    svm = SVC(kernel="rbf", probability=True, random_state=42)
    lr  = LogisticRegression(max_iter=1000, random_state=42)

    ensemble = VotingClassifier(
        estimators=[("rf", rf), ("svm", svm), ("lr", lr)],
        voting="soft"
    )
    ensemble.fit(X_train, y_train)

    acc = ensemble.score(X_test, y_test)
    print(f"[BehaviourModel] Test accuracy: {acc:.3f}")

    # Save model and scaler
    with open(MODEL_PATH,  "wb") as f: pickle.dump(ensemble, f)
    with open(SCALER_PATH, "wb") as f: pickle.dump(scaler,   f)
    print("[BehaviourModel] Model saved.")
    return ensemble, scaler


def load_behaviour_model():
    """Load the saved model, or train a new one if not found."""
    if os.path.exists(MODEL_PATH) and os.path.exists(SCALER_PATH):
        with open(MODEL_PATH,  "rb") as f: model  = pickle.load(f)
        with open(SCALER_PATH, "rb") as f: scaler = pickle.load(f)
        print("[BehaviourModel] Loaded from disk.")
        return model, scaler
    else:
        print("[BehaviourModel] No saved model found, training...")
        return train_behaviour_model()


class BehaviourClassifier:
    def __init__(self):
        self.model, self.scaler = load_behaviour_model()

    def predict(self, feature_vector: np.ndarray) -> dict:
        """
        Predict behaviour class and probabilities.
        Returns dict with 'class', 'label', 'probabilities'.
        """
        X = feature_vector.reshape(1, -1)
        X_scaled = self.scaler.transform(X)
        proba = self.model.predict_proba(X_scaled)[0]
        pred  = int(np.argmax(proba))
        labels = {0: "Normal", 1: "Suspicious", 2: "Cheating"}
        return {
            "class":         pred,
            "label":         labels[pred],
            "prob_normal":     float(proba[0]),
            "prob_suspicious": float(proba[1]),
            "prob_cheating":   float(proba[2]),
        }
