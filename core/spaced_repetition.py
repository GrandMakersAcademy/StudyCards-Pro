"""
Spaced Repetition (SM-2) Algorithm for StudyCards-Pro
Manages review intervals for flashcards to maximize memory retention
"""
from datetime import datetime, timedelta

class SpacedRepetition:
    """Implements the SM-2 algorithm for scheduling flashcard reviews."""
    DEFAULT_EASINESS = 2.5
    MIN_EASINESS = 1.3

    @staticmethod
    def get_next_review(card_progress, quality):
        # card_progress is a dict with repetitions, interval, easiness_factor, next_review_date
        ef = card_progress.get('easiness_factor', SpacedRepetition.DEFAULT_EASINESS)
        repetitions = card_progress.get('repetitions', 0)
        interval = card_progress.get('interval', 0)
        if quality < 3:
            repetitions = 0
            interval = 1
        else:
            repetitions += 1
            if repetitions == 1:
                interval = 1
            elif repetitions == 2:
                interval = 3
            else:
                interval = round(interval * ef)
            # Update easiness factor
            ef = max(SpacedRepetition.MIN_EASINESS, ef + (0.1 - (5 - quality) * (0.08 + (5 - quality) * 0.02)))
        next_review_date = (datetime.now() + timedelta(days=interval)).date()
        return {
            'repetitions': repetitions,
            'interval': interval,
            'easiness_factor': ef,
            'next_review_date': str(next_review_date)
        }
