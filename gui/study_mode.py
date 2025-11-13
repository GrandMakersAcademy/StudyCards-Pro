"""
Study mode tab for StudyCards-Pro
"""
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton

class StudyMode(QWidget):
    def __init__(self, db):
        super().__init__()
        layout = QVBoxLayout(self)
        self.label = QLabel("Start a study session!")
        layout.addWidget(self.label)
        self.start_btn = QPushButton("Begin Study")
        layout.addWidget(self.start_btn)
        self.db = db
