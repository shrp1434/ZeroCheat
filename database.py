"""
database.py
Handles all SQLite database operations.
Creates all tables on first run.
"""

import sqlite3
import os

DB_PATH = "exam_monitor.db"

def get_connection():
    """Return a connection to the SQLite database."""
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row  # allows dict-like access to rows
    return conn

def init_db():
    """Create all database tables if they don't exist."""
    conn = get_connection()
    c = conn.cursor()

    # Users table - stores registered exam takers
    c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            full_name TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Face encodings - 128-d face_recognition vector stored as binary blob
    c.execute("""
        CREATE TABLE IF NOT EXISTS face_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            encoding BLOB NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)

    # Iris features stored as binary blob
    c.execute("""
        CREATE TABLE IF NOT EXISTS iris_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            left_features BLOB,
            right_features BLOB,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)

    # Keystroke timing data
    c.execute("""
        CREATE TABLE IF NOT EXISTS keystroke_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            avg_hold_time REAL,
            avg_flight_time REAL,
            typing_speed REAL,
            error_rate REAL,
            profile_blob BLOB,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)

    # Mouse movement data
    c.execute("""
        CREATE TABLE IF NOT EXISTS mouse_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            avg_speed REAL,
            avg_acceleration REAL,
            click_interval REAL,
            profile_blob BLOB,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)

    # Exam sessions
    c.execute("""
        CREATE TABLE IF NOT EXISTS exam_sessions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            start_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            end_time TIMESTAMP,
            final_risk_score REAL,
            final_cheating_prob REAL,
            status TEXT DEFAULT 'active',
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)

    # Per-frame behaviour features (stored every N seconds)
    c.execute("""
        CREATE TABLE IF NOT EXISTS behaviour_features (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id INTEGER,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            gaze_direction TEXT,
            head_pitch REAL,
            head_yaw REAL,
            head_roll REAL,
            blink_rate REAL,
            mouth_open_freq REAL,
            shoulder_movement REAL,
            hand_movement REAL,
            phone_detected INTEGER DEFAULT 0,
            person_count INTEGER DEFAULT 1,
            typing_speed REAL,
            mouse_speed REAL,
            time_looking_away REAL,
            object_count INTEGER DEFAULT 0,
            FOREIGN KEY (session_id) REFERENCES exam_sessions(id)
        )
    """)

    # Anomaly scores from Isolation Forest / One-Class SVM
    c.execute("""
        CREATE TABLE IF NOT EXISTS anomaly_scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id INTEGER,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            isolation_score REAL,
            svm_score REAL,
            is_anomaly INTEGER DEFAULT 0,
            FOREIGN KEY (session_id) REFERENCES exam_sessions(id)
        )
    """)

    # Risk scores calculated by risk engine
    c.execute("""
        CREATE TABLE IF NOT EXISTS risk_scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id INTEGER,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            risk_score REAL,
            cheating_probability REAL,
            identity_confidence REAL,
            FOREIGN KEY (session_id) REFERENCES exam_sessions(id)
        )
    """)

    # Alert events (e.g., phone detected, face not found)
    c.execute("""
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id INTEGER,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            event_type TEXT,
            severity TEXT,
            description TEXT,
            screenshot_path TEXT,
            FOREIGN KEY (session_id) REFERENCES exam_sessions(id)
        )
    """)

    # Final generated reports
    c.execute("""
        CREATE TABLE IF NOT EXISTS reports (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id INTEGER,
            user_id INTEGER,
            generated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            pdf_path TEXT,
            FOREIGN KEY (session_id) REFERENCES exam_sessions(id)
        )
    """)

    conn.commit()
    conn.close()
    print("[DB] Database initialised successfully.")

# Helper functions used across modules

def insert_user(username, full_name):
    conn = get_connection()
    c = conn.cursor()
    c.execute("INSERT INTO users (username, full_name) VALUES (?, ?)", (username, full_name))
    conn.commit()
    user_id = c.lastrowid
    conn.close()
    return user_id

def get_user_by_username(username):
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = ?", (username,))
    row = c.fetchone()
    conn.close()
    return dict(row) if row else None

def get_all_users():
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    rows = c.fetchall()
    conn.close()
    return [dict(r) for r in rows]

def insert_event(session_id, event_type, severity, description, screenshot_path=None):
    conn = get_connection()
    c = conn.cursor()
    c.execute("""
        INSERT INTO events (session_id, event_type, severity, description, screenshot_path)
        VALUES (?, ?, ?, ?, ?)
    """, (session_id, event_type, severity, description, screenshot_path))
    conn.commit()
    conn.close()

def get_events_for_session(session_id):
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM events WHERE session_id = ? ORDER BY timestamp", (session_id,))
    rows = c.fetchall()
    conn.close()
    return [dict(r) for r in rows]

def start_session(user_id):
    conn = get_connection()
    c = conn.cursor()
    c.execute("INSERT INTO exam_sessions (user_id) VALUES (?)", (user_id,))
    conn.commit()
    session_id = c.lastrowid
    conn.close()
    return session_id

def end_session(session_id, risk_score, cheating_prob):
    conn = get_connection()
    c = conn.cursor()
    c.execute("""
        UPDATE exam_sessions
        SET end_time = CURRENT_TIMESTAMP,
            final_risk_score = ?,
            final_cheating_prob = ?,
            status = 'completed'
        WHERE id = ?
    """, (risk_score, cheating_prob, session_id))
    conn.commit()
    conn.close()

def insert_risk_score(session_id, risk_score, cheating_prob, identity_conf):
    conn = get_connection()
    c = conn.cursor()
    c.execute("""
        INSERT INTO risk_scores (session_id, risk_score, cheating_probability, identity_confidence)
        VALUES (?, ?, ?, ?)
    """, (session_id, risk_score, cheating_prob, identity_conf))
    conn.commit()
    conn.close()

def insert_behaviour_features(session_id, features: dict):
    conn = get_connection()
    c = conn.cursor()
    c.execute("""
        INSERT INTO behaviour_features
        (session_id, gaze_direction, head_pitch, head_yaw, head_roll,
         blink_rate, mouth_open_freq, shoulder_movement, hand_movement,
         phone_detected, person_count, typing_speed, mouse_speed,
         time_looking_away, object_count)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
    """, (
        session_id,
        features.get("gaze_direction", "center"),
        features.get("head_pitch", 0.0),
        features.get("head_yaw", 0.0),
        features.get("head_roll", 0.0),
        features.get("blink_rate", 0.0),
        features.get("mouth_open_freq", 0.0),
        features.get("shoulder_movement", 0.0),
        features.get("hand_movement", 0.0),
        features.get("phone_detected", 0),
        features.get("person_count", 1),
        features.get("typing_speed", 0.0),
        features.get("mouse_speed", 0.0),
        features.get("time_looking_away", 0.0),
        features.get("object_count", 0),
    ))
    conn.commit()
    conn.close()

def get_risk_scores_for_session(session_id):
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM risk_scores WHERE session_id=? ORDER BY timestamp", (session_id,))
    rows = c.fetchall()
    conn.close()
    return [dict(r) for r in rows]

def get_all_sessions():
    conn = get_connection()
    c = conn.cursor()
    c.execute("""
        SELECT es.*, u.username, u.full_name
        FROM exam_sessions es
        JOIN users u ON es.user_id = u.id
        ORDER BY es.start_time DESC
    """)
    rows = c.fetchall()
    conn.close()
    return [dict(r) for r in rows]

if __name__ == "__main__":
    init_db()
