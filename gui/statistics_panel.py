"""
Statistics panel tab for StudyCards-Pro
"""
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel

class StatisticsPanel(QWidget):
    def __init__(self, db):
        super().__init__()
        layout = QVBoxLayout(self)
        self.label = QLabel("Statistics will appear here.")
        layout.addWidget(self.label)
        self.db = db
