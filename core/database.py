"""Database management for StudyCards-Pro"""

import sqlite3
import json
import csv
from datetime import datetime
from typing import List, Dict, Optional, Tuple
from pathlib import Path


class Database:
    """Manages SQLite database operations for flashcards"""
    
    def __init__(self, db_path: str = "studycards.db"):
        self.db_path = db_path
        self.conn = None
        
    def initialize(self):
        """Initialize database connection and create tables"""
        self.conn = sqlite3.connect(self.db_path)
        self.conn.row_factory = sqlite3.Row
        self._create_tables()
        self._insert_default_categories()
        
    def _create_tables(self):
        """Create database schema"""
        cursor = self.conn.cursor()
        
        # Categories table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS categories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                color TEXT DEFAULT '#3498db',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Decks table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS decks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                category_id INTEGER,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (category_id) REFERENCES categories(id)
            )
        """)
        
        # Cards table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS cards (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                deck_id INTEGER NOT NULL,
                question TEXT NOT NULL,
                answer TEXT NOT NULL,
                example TEXT,
                tags TEXT,
                difficulty INTEGER DEFAULT 0,
                ease_factor REAL DEFAULT 2.5,
                interval INTEGER DEFAULT 0,
                repetitions INTEGER DEFAULT 0,
                next_review DATE,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (deck_id) REFERENCES decks(id) ON DELETE CASCADE
            )
        """)
        
        # Review history table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS review_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                card_id INTEGER NOT NULL,
                quality INTEGER NOT NULL,
                reviewed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                time_spent INTEGER,
                FOREIGN KEY (card_id) REFERENCES cards(id) ON DELETE CASCADE
            )
        """)
        
        self.conn.commit()
        
    def _insert_default_categories(self):
        """Insert default categories if they don't exist"""
        cursor = self.conn.cursor()
        default_categories = [
            ('Mathematics', '#e74c3c'),
            ('English', '#3498db'),
            ('History', '#9b59b6'),
            ('Science', '#2ecc71'),
            ('Geography', '#f39c12'),
            ('Programming', '#34495e'),
            ('General', '#95a5a6')
        ]
        
        for name, color in default_categories:
            cursor.execute(
                "INSERT OR IGNORE INTO categories (name, color) VALUES (?, ?)",
                (name, color)
            )
        self.conn.commit()
        
    # Category operations
    def get_all_categories(self) -> List[Dict]:
        """Get all categories"""
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM categories ORDER BY name")
        return [dict(row) for row in cursor.fetchall()]
        
    def add_category(self, name: str, color: str = '#3498db') -> int:
        """Add a new category"""
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO categories (name, color) VALUES (?, ?)",
            (name, color)
        )
        self.conn.commit()
        return cursor.lastrowid
        
    # Deck operations
    def get_all_decks(self, category_id: Optional[int] = None) -> List[Dict]:
        """Get all decks, optionally filtered by category"""
        cursor = self.conn.cursor()
        if category_id:
            cursor.execute(
                """SELECT d.*, c.name as category_name, c.color as category_color,
                   COUNT(DISTINCT cards.id) as card_count,
                   COUNT(CASE WHEN cards.next_review <= date('now') THEN 1 END) as due_count
                   FROM decks d 
                   LEFT JOIN categories c ON d.category_id = c.id
                   LEFT JOIN cards ON d.id = cards.deck_id
                   WHERE d.category_id = ?
                   GROUP BY d.id
                   ORDER BY d.name""",
                (category_id,)
            )
        else:
            cursor.execute(
                """SELECT d.*, c.name as category_name, c.color as category_color,
                   COUNT(DISTINCT cards.id) as card_count,
                   COUNT(CASE WHEN cards.next_review <= date('now') THEN 1 END) as due_count
                   FROM decks d 
                   LEFT JOIN categories c ON d.category_id = c.id
                   LEFT JOIN cards ON d.id = cards.deck_id
                   GROUP BY d.id
                   ORDER BY d.name"""
            )
        return [dict(row) for row in cursor.fetchall()]
        
    def add_deck(self, name: str, category_id: int, description: str = "") -> int:
        """Add a new deck"""
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO decks (name, description, category_id) VALUES (?, ?, ?)",
            (name, description, category_id)
        )
        self.conn.commit()
        return cursor.lastrowid
        
    def update_deck(self, deck_id: int, name: str, description: str, category_id: int):
        """Update deck information"""
        cursor = self.conn.cursor()
        cursor.execute(
            "UPDATE decks SET name = ?, description = ?, category_id = ? WHERE id = ?",
            (name, description, category_id, deck_id)
        )
        self.conn.commit()
        
    def delete_deck(self, deck_id: int):
        """Delete a deck and all its cards"""
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM decks WHERE id = ?", (deck_id,))
        self.conn.commit()
        
    # Card operations
    def get_cards_by_deck(self, deck_id: int) -> List[Dict]:
        """Get all cards in a deck"""
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT * FROM cards WHERE deck_id = ? ORDER BY created_at DESC",
            (deck_id,)
        )
        return [dict(row) for row in cursor.fetchall()]
        
    def get_due_cards(self, deck_id: Optional[int] = None) -> List[Dict]:
        """Get cards due for review"""
        cursor = self.conn.cursor()
        if deck_id:
            cursor.execute(
                """SELECT * FROM cards 
                   WHERE deck_id = ? AND (next_review IS NULL OR next_review <= date('now'))
                   ORDER BY next_review""",
                (deck_id,)
            )
        else:
            cursor.execute(
                """SELECT * FROM cards 
                   WHERE next_review IS NULL OR next_review <= date('now')
                   ORDER BY next_review"""
            )
        return [dict(row) for row in cursor.fetchall()]
        
    def add_card(self, deck_id: int, question: str, answer: str, 
                 example: str = "", tags: str = "") -> int:
        """Add a new card"""
        cursor = self.conn.cursor()
        cursor.execute(
            """INSERT INTO cards (deck_id, question, answer, example, tags)
               VALUES (?, ?, ?, ?, ?)""",
            (deck_id, question, answer, example, tags)
        )
        self.conn.commit()
        return cursor.lastrowid
        
    def update_card(self, card_id: int, question: str, answer: str, 
                    example: str = "", tags: str = ""):
        """Update card content"""
        cursor = self.conn.cursor()
        cursor.execute(
            """UPDATE cards SET question = ?, answer = ?, example = ?, tags = ?,
               updated_at = CURRENT_TIMESTAMP WHERE id = ?""",
            (question, answer, example, tags, card_id)
        )
        self.conn.commit()
        
    def update_card_review_data(self, card_id: int, ease_factor: float, 
                                interval: int, repetitions: int, next_review: str):
        """Update card's spaced repetition data"""
        cursor = self.conn.cursor()
        cursor.execute(
            """UPDATE cards SET ease_factor = ?, interval = ?, repetitions = ?, 
               next_review = ? WHERE id = ?""",
            (ease_factor, interval, repetitions, next_review, card_id)
        )
        self.conn.commit()
        
    def delete_card(self, card_id: int):
        """Delete a card"""
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM cards WHERE id = ?", (card_id,))
        self.conn.commit()
        
    def add_review(self, card_id: int, quality: int, time_spent: int = 0):
        """Record a review in history"""
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO review_history (card_id, quality, time_spent) VALUES (?, ?, ?)",
            (card_id, quality, time_spent)
        )
        self.conn.commit()
        
    # Statistics
    def get_review_stats(self, days: int = 30) -> Dict:
        """Get review statistics for the last N days"""
        cursor = self.conn.cursor()
        cursor.execute(
            """SELECT DATE(reviewed_at) as date, COUNT(*) as count,
               AVG(quality) as avg_quality
               FROM review_history
               WHERE reviewed_at >= date('now', '-' || ? || ' days')
               GROUP BY DATE(reviewed_at)
               ORDER BY date""",
            (days,)
        )
        return [dict(row) for row in cursor.fetchall()]
        
    def get_total_cards(self) -> int:
        """Get total number of cards"""
        cursor = self.conn.cursor()
        cursor.execute("SELECT COUNT(*) as count FROM cards")
        return cursor.fetchone()['count']
        
    def get_total_reviews(self) -> int:
        """Get total number of reviews"""
        cursor = self.conn.cursor()
        cursor.execute("SELECT COUNT(*) as count FROM review_history")
        return cursor.fetchone()['count']
        
    # Import/Export
    def export_deck_to_csv(self, deck_id: int, filepath: str):
        """Export deck to CSV file"""
        cards = self.get_cards_by_deck(deck_id)
        with open(filepath, 'w', newline='', encoding='utf-8') as f:
            if cards:
                writer = csv.DictWriter(f, fieldnames=cards[0].keys())
                writer.writeheader()
                writer.writerows(cards)
                
    def import_deck_from_csv(self, deck_id: int, filepath: str):
        """Import cards from CSV file"""
        with open(filepath, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                self.add_card(
                    deck_id,
                    row.get('question', ''),
                    row.get('answer', ''),
                    row.get('example', ''),
                    row.get('tags', '')
                )
                
    def close(self):
        """Close database connection"""
        if self.conn:
            self.conn.close()
