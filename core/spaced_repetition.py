"""Spaced Repetition Algorithm (SuperMemo 2) Implementation"""

from datetime import datetime, timedelta
from typing import Tuple


class SpacedRepetitionEngine:
    """Implements the SuperMemo 2 (SM-2) spaced repetition algorithm"""
    
    @staticmethod
    def calculate_next_review(ease_factor: float, interval: int, repetitions: int, 
                              quality: int) -> Tuple[float, int, int, str]:
        """
        Calculate next review parameters based on SM-2 algorithm
        
        Args:
            ease_factor: Current ease factor (usually starts at 2.5)
            interval: Current interval in days
            repetitions: Number of consecutive correct repetitions
            quality: Quality of response (0-5)
                     0 = Complete blackout
                     1 = Incorrect, but familiar
                     2 = Incorrect, but close
                     3 = Correct with difficulty
                     4 = Correct with hesitation
                     5 = Perfect recall
        
        Returns:
            Tuple of (new_ease_factor, new_interval, new_repetitions, next_review_date)
        """
        
        # Quality must be between 0 and 5
        quality = max(0, min(5, quality))
        
        # If quality is less than 3, reset the repetitions
        if quality < 3:
            new_repetitions = 0
            new_interval = 1
        else:
            # Update ease factor
            new_ease_factor = ease_factor + (0.1 - (5 - quality) * (0.08 + (5 - quality) * 0.02))
            new_ease_factor = max(1.3, new_ease_factor)  # Minimum ease factor is 1.3
            
            # Calculate new interval
            if repetitions == 0:
                new_interval = 1
                new_repetitions = 1
            elif repetitions == 1:
                new_interval = 6
                new_repetitions = 2
            else:
                new_interval = round(interval * new_ease_factor)
                new_repetitions = repetitions + 1
            
            ease_factor = new_ease_factor
        
        if quality < 3:
            new_repetitions = 0
            new_interval = 1
        
        # Calculate next review date
        next_review = datetime.now() + timedelta(days=new_interval)
        next_review_str = next_review.strftime('%Y-%m-%d')
        
        return (ease_factor, new_interval, new_repetitions, next_review_str)
    
    @staticmethod
    def get_quality_from_button(button_index: int) -> int:
        """
        Convert button press to quality rating
        
        Args:
            button_index: 0 = Again, 1 = Hard, 2 = Good, 3 = Easy
        
        Returns:
            Quality rating (0-5)
        """
        quality_map = {
            0: 0,  # Again - Complete failure
            1: 3,  # Hard - Correct with difficulty
            2: 4,  # Good - Correct with some hesitation
            3: 5   # Easy - Perfect recall
        }
        return quality_map.get(button_index, 4)
    
    @staticmethod
    def get_interval_text(interval: int) -> str:
        """
        Get human-readable text for interval
        
        Args:
            interval: Interval in days
        
        Returns:
            Human-readable interval string
        """
        if interval < 1:
            return "< 1 day"
        elif interval == 1:
            return "1 day"
        elif interval < 7:
            return f"{interval} days"
        elif interval < 30:
            weeks = interval // 7
            return f"{weeks} week{'s' if weeks > 1 else ''}"
        elif interval < 365:
            months = interval // 30
            return f"{months} month{'s' if months > 1 else ''}"
        else:
            years = interval // 365
            return f"{years} year{'s' if years > 1 else ''}"
    
    @staticmethod
    def get_button_intervals(ease_factor: float, interval: int, repetitions: int) -> dict:
        """
        Get preview intervals for each button
        
        Args:
            ease_factor: Current ease factor
            interval: Current interval
            repetitions: Current repetitions
        
        Returns:
            Dictionary with intervals for each button
        """
        intervals = {}
        
        for button_idx in range(4):
            quality = SpacedRepetitionEngine.get_quality_from_button(button_idx)
            _, new_interval, _, _ = SpacedRepetitionEngine.calculate_next_review(
                ease_factor, interval, repetitions, quality
            )
            intervals[button_idx] = SpacedRepetitionEngine.get_interval_text(new_interval)
        
        return intervals
