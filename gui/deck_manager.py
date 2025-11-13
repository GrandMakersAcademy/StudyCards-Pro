"""
Deck manager tab for StudyCards-Pro
"""
from PySide6.QtWidgets import QWidget, QVBoxLayout, QListWidget
from core.models import Deck

class DeckManager(QWidget):
    def __init__(self, db):
        super().__init__()
        layout = QVBoxLayout(self)
        self.deck_list = QListWidget()
        layout.addWidget(self.deck_list)
        self.db = db
        self.refresh()

    def refresh(self):
        self.deck_list.clear()
        for deck in self.db.get_all_decks():
            self.deck_list.addItem(f"{deck['name']} ({deck['card_count']} cards)")
