#!/usr/bin/env python3
"""
StudyCards-Pro - Advanced Flashcard Learning System
Main application entry point
"""

import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt
import qdarkstyle

from gui.main_window import MainWindow
from core.database import Database


def main():
    """Initialize and run the application"""
    # Enable High DPI scaling
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough
    )
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    
    # Create application
    app = QApplication(sys.argv)
    app.setApplicationName("StudyCards-Pro")
    app.setOrganizationName("GrandMakersAcademy")
    
    # Apply dark theme
    app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyside6'))
    
    # Initialize database
    db = Database()
    db.initialize()
    
    # Create and show main window
    window = MainWindow(db)
    window.show()
    
    # Run application
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
