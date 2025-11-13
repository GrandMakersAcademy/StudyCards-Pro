"""
Main Window for StudyCards-Pro
Implements main UI: navigation, dashboard, and controls
"""
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QTabWidget
from gui.card_editor import CardEditor
from gui.study_session import StudySession
from gui.statistics import StatisticsView
from gui.category_manager import CategoryManager

class MainWindow(QMainWindow):
    def __init__(self, db_manager):
        super().__init__()
        self.setWindowTitle("StudyCards-Pro")
        self.db_manager = db_manager
        self.resize(900, 640)
        self.tabs = QTabWidget(self)
        self.setCentralWidget(self.tabs)
        self.init_tabs()

    def init_tabs(self):
        self.tabs.addTab(StudySession(self.db_manager), "Study")
        self.tabs.addTab(CardEditor(self.db_manager), "Cards")
        self.tabs.addTab(CategoryManager(self.db_manager), "Categories")
        self.tabs.addTab(StatisticsView(self.db_manager), "Statistics")
