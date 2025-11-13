"""Statistics and analytics for StudyCards-Pro"""

from typing import Dict, List, Tuple
from datetime import datetime, timedelta
from collections import defaultdict


class StatisticsEngine:
    """Provides statistical analysis of study progress"""
    
    def __init__(self, database):
        self.db = database
    
    def get_daily_stats(self, days: int = 7) -> List[Dict]:
        """
        Get daily review statistics
        
        Args:
            days: Number of days to look back
        
        Returns:
            List of daily statistics
        """
        stats = self.db.get_review_stats(days)
        
        # Fill in missing days with zero counts
        result = []
        for i in range(days):
            date = (datetime.now() - timedelta(days=days-i-1)).strftime('%Y-%m-%d')
            found = False
            for stat in stats:
                if stat['date'] == date:
                    result.append(stat)
                    found = True
                    break
            if not found:
                result.append({
                    'date': date,
                    'count': 0,
                    'avg_quality': 0
                })
        
        return result
    
    def get_category_distribution(self) -> List[Dict]:
        """
        Get distribution of cards across categories
        
        Returns:
            List of category statistics
        """
        cursor = self.db.conn.cursor()
        cursor.execute("""
            SELECT c.name, c.color, COUNT(cards.id) as count
            FROM categories c
            LEFT JOIN decks d ON c.id = d.category_id
            LEFT JOIN cards ON d.id = cards.deck_id
            GROUP BY c.id
            HAVING count > 0
            ORDER BY count DESC
        """)
        return [dict(row) for row in cursor.fetchall()]
    
    def get_success_rate(self, days: int = 30) -> float:
        """
        Calculate success rate (quality >= 3) for recent reviews
        
        Args:
            days: Number of days to look back
        
        Returns:
            Success rate as percentage (0-100)
        """
        cursor = self.db.conn.cursor()
        cursor.execute("""
            SELECT 
                COUNT(CASE WHEN quality >= 3 THEN 1 END) * 100.0 / COUNT(*) as rate
            FROM review_history
            WHERE reviewed_at >= date('now', '-' || ? || ' days')
        """, (days,))
        
        result = cursor.fetchone()
        return round(result['rate'], 1) if result and result['rate'] else 0.0
    
    def get_study_streak(self) -> int:
        """
        Calculate current study streak in days
        
        Returns:
            Number of consecutive days studied
        """
        cursor = self.db.conn.cursor()
        cursor.execute("""
            SELECT DISTINCT DATE(reviewed_at) as date
            FROM review_history
            ORDER BY date DESC
            LIMIT 100
        """)
        
        dates = [row['date'] for row in cursor.fetchall()]
        if not dates:
            return 0
        
        streak = 0
        check_date = datetime.now().date()
        
        for date_str in dates:
            date = datetime.strptime(date_str, '%Y-%m-%d').date()
            if date == check_date:
                streak += 1
                check_date -= timedelta(days=1)
            elif date < check_date:
                break
        
        return streak
    
    def get_cards_due_today(self) -> int:
        """
        Get number of cards due for review today
        
        Returns:
            Number of due cards
        """
        due_cards = self.db.get_due_cards()
        return len(due_cards)
    
    def get_mastery_level(self) -> Dict[str, int]:
        """
        Get distribution of cards by mastery level
        
        Returns:
            Dictionary with counts for each mastery level
        """
        cursor = self.db.conn.cursor()
        cursor.execute("""
            SELECT 
                CASE 
                    WHEN repetitions = 0 THEN 'new'
                    WHEN repetitions <= 2 THEN 'learning'
                    WHEN repetitions <= 5 THEN 'young'
                    ELSE 'mature'
                END as level,
                COUNT(*) as count
            FROM cards
            GROUP BY level
        """)
        
        result = {'new': 0, 'learning': 0, 'young': 0, 'mature': 0}
        for row in cursor.fetchall():
            result[row['level']] = row['count']
        
        return result
    
    def get_difficult_cards(self, limit: int = 10) -> List[Dict]:
        """
        Get cards with lowest ease factors (most difficult)
        
        Args:
            limit: Maximum number of cards to return
        
        Returns:
            List of difficult cards
        """
        cursor = self.db.conn.cursor()
        cursor.execute("""
            SELECT c.*, d.name as deck_name
            FROM cards c
            JOIN decks d ON c.deck_id = d.id
            WHERE c.repetitions > 0
            ORDER BY c.ease_factor ASC, c.repetitions DESC
            LIMIT ?
        """, (limit,))
        return [dict(row) for row in cursor.fetchall()]
    
    def get_total_study_time(self, days: int = 30) -> int:
        """
        Get total study time in minutes
        
        Args:
            days: Number of days to look back
        
        Returns:
            Total study time in minutes
        """
        cursor = self.db.conn.cursor()
        cursor.execute("""
            SELECT SUM(time_spent) as total
            FROM review_history
            WHERE reviewed_at >= date('now', '-' || ? || ' days')
        """, (days,))
        
        result = cursor.fetchone()
        total_seconds = result['total'] if result and result['total'] else 0
        return round(total_seconds / 60)
    
    def get_weekly_heatmap(self) -> List[Tuple[str, int]]:
        """
        Get review activity heatmap for the past 12 weeks
        
        Returns:
            List of (date, count) tuples
        """
        cursor = self.db.conn.cursor()
        cursor.execute("""
            SELECT DATE(reviewed_at) as date, COUNT(*) as count
            FROM review_history
            WHERE reviewed_at >= date('now', '-84 days')
            GROUP BY DATE(reviewed_at)
            ORDER BY date
        """)
        
        return [(row['date'], row['count']) for row in cursor.fetchall()]
