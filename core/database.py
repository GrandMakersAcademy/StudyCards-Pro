"""
Database management for StudyCards-Pro
Handles all SQLite database operations
"""

import sqlite3
from datetime import datetime, timedelta
from pathlib import Path
from typing import List, Optional, Dict, Any

class DatabaseManager:
    """Manages SQLite database operations for flashcards"""
    
    def __init__(self, db_path: str = "studycards.db"):
        self.db_path = db_path
        self.conn = None
        
    def connect(self):
        self.conn = sqlite3.connect(self.db_path)
        self.conn.row_factory = sqlite3.Row
        return self.conn
    
    def initialize_database(self):
        conn = self.connect()
        cursor = conn.cursor()
        # Categories table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS categories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                description TEXT,
                color TEXT DEFAULT '#3498db',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        # Flashcards table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS flashcards (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                category_id INTEGER NOT NULL,
                front TEXT NOT NULL,
                back TEXT NOT NULL,
                example TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE CASCADE
            )
        """)
        # Spaced repetition data table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS card_progress (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                card_id INTEGER NOT NULL,
                easiness_factor REAL DEFAULT 2.5,
                interval INTEGER DEFAULT 0,
                repetitions INTEGER DEFAULT 0,
                next_review_date DATE,
                last_reviewed TIMESTAMP,
                total_reviews INTEGER DEFAULT 0,
                correct_reviews INTEGER DEFAULT 0,
                FOREIGN KEY (card_id) REFERENCES flashcards(id) ON DELETE CASCADE
            )
        """)
        # Study sessions table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS study_sessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                card_id INTEGER NOT NULL,
                quality INTEGER NOT NULL,
                session_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (card_id) REFERENCES flashcards(id) ON DELETE CASCADE
            )
        """)
        # Create indexes for performance
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_card_category 
            ON flashcards(category_id)
        """)
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_progress_card 
            ON card_progress(card_id)
        """)
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_progress_review_date 
            ON card_progress(next_review_date)
        """)
        conn.commit()
        cursor.execute("SELECT COUNT(*) FROM categories")
        if cursor.fetchone()[0] == 0:
            self._add_default_categories(cursor)
            conn.commit()
    def _add_default_categories(self, cursor):
        default_categories = [
            ("Mathematics", "Math formulas, theorems, and concepts", "#e74c3c"),
            ("English", "Vocabulary, grammar, and phrases", "#3498db"),
            ("History", "Historical dates, events, and figures", "#f39c12"),
            ("Science", "Scientific concepts and definitions", "#2ecc71"),
            ("Programming", "Code snippets and programming concepts", "#9b59b6")
        ]
        cursor.executemany(
            "INSERT INTO categories (name, description, color) VALUES (?, ?, ?)",
            default_categories
        )