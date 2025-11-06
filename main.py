#!/usr/bin/env python3
"""
StudyCards Pro - Advanced Flashcard Application with Spaced Repetition
A comprehensive learning tool for students and educators.

Author: GrandMakersAcademy
Version: 1.0.0
License: MIT
"""

import sys
import os
from pathlib import Path

# Add the src directory to Python path
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
import qdarkstyle

from gui.main_window import MainWindow
from core.database import DatabaseManager

def main():
    """Main entry point for the application."""
    # Create QApplication instance
    app = QApplication(sys.argv)
    
    # Set application properties
    app.setApplicationName("StudyCards Pro")
    app.setApplicationVersion("1.0.0")
    app.setOrganizationName("GrandMakersAcademy")
    
    # Apply dark theme
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())
    
    # Set application icon if available
    icon_path = Path(__file__).parent / "assets" / "icon.ico"
    if icon_path.exists():
        app.setWindowIcon(QIcon(str(icon_path)))
    
    # Initialize database
    db_manager = DatabaseManager()
    db_manager.initialize_database()
    
    # Create and show main window
    window = MainWindow(db_manager)
    window.show()
    
    # Start the event loop
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
