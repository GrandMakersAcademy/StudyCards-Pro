"""
Dialog modules for StudyCards-Pro
"""
from PySide6.QtWidgets import QDialog

class InfoDialog(QDialog):
    def __init__(self, text):
        super().__init__()
        self.setWindowTitle("Info")
        # Add additional UI setup as needed
