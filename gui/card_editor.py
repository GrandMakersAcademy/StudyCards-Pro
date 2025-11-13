"""
Card editor tab for StudyCards-Pro
"""
from PySide6.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QLineEdit, QPushButton, QLabel

class CardEditor(QWidget):
    def __init__(self, db):
        super().__init__()
        layout = QVBoxLayout(self)
        self.question = QLineEdit()
        self.answer = QLineEdit()
        self.example = QTextEdit()
        self.save_btn = QPushButton("Save Card")
        layout.addWidget(QLabel("Question"))
        layout.addWidget(self.question)
        layout.addWidget(QLabel("Answer"))
        layout.addWidget(self.answer)
        layout.addWidget(QLabel("Example"))
        layout.addWidget(self.example)
        layout.addWidget(self.save_btn)
        self.db = db
