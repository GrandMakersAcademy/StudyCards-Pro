"""Data models for StudyCards-Pro"""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List


@dataclass
class Category:
    """Category model"""
    id: int
    name: str
    color: str
    created_at: datetime
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Category':
        return cls(
            id=data['id'],
            name=data['name'],
            color=data['color'],
            created_at=datetime.fromisoformat(data['created_at'])
        )


@dataclass
class Deck:
    """Deck model"""
    id: int
    name: str
    description: str
    category_id: int
    category_name: Optional[str] = None
    category_color: Optional[str] = None
    card_count: int = 0
    due_count: int = 0
    created_at: Optional[datetime] = None
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Deck':
        return cls(
            id=data['id'],
            name=data['name'],
            description=data.get('description', ''),
            category_id=data['category_id'],
            category_name=data.get('category_name'),
            category_color=data.get('category_color'),
            card_count=data.get('card_count', 0),
            due_count=data.get('due_count', 0),
            created_at=datetime.fromisoformat(data['created_at']) if data.get('created_at') else None
        )


@dataclass
class Card:
    """Flashcard model"""
    id: int
    deck_id: int
    question: str
    answer: str
    example: str = ""
    tags: str = ""
    difficulty: int = 0
    ease_factor: float = 2.5
    interval: int = 0
    repetitions: int = 0
    next_review: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Card':
        return cls(
            id=data['id'],
            deck_id=data['deck_id'],
            question=data['question'],
            answer=data['answer'],
            example=data.get('example', ''),
            tags=data.get('tags', ''),
            difficulty=data.get('difficulty', 0),
            ease_factor=data.get('ease_factor', 2.5),
            interval=data.get('interval', 0),
            repetitions=data.get('repetitions', 0),
            next_review=data.get('next_review'),
            created_at=datetime.fromisoformat(data['created_at']) if data.get('created_at') else None,
            updated_at=datetime.fromisoformat(data['updated_at']) if data.get('updated_at') else None
        )
    
    def get_tags_list(self) -> List[str]:
        """Get tags as a list"""
        return [tag.strip() for tag in self.tags.split(',') if tag.strip()]
