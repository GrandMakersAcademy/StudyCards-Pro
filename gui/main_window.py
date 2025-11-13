"""
Main application window for StudyCards-Pro
"""
from PySide6.QtWidgets import QMainWindow, QTabWidget, QVBoxLayout, QWidget, QStatusBar, QAction, QMenuBar
from PySide6.QtGui import QIcon
from gui.deck_manager import DeckManager
from gui.study_mode import StudyMode
from gui.statistics_panel import StatisticsPanel

class MainWindow(QMainWindow):
    def __init__(self, db):
        super().__init__()
        self.setWindowTitle("StudyCards-Pro")
        self.setWindowIcon(QIcon(":/icon.png"))
        self.resize(1000, 720)

        self.db = db

        self.tabs = QTabWidget()
        self.tabs.addTab(DeckManager(db), "Decks")
        self.tabs.addTab(StudyMode(db), "Study")
        self.tabs.addTab(StatisticsPanel(db), "Statistics")

        central = QWidget()
        layout = QVBoxLayout(central)
        layout.addWidget(self.tabs)
        self.setCentralWidget(central)

        self.setStatusBar(QStatusBar())
        self.setup_menu()

    def setup_menu(self):
        menubar = QMenuBar(self)
        file_menu = menubar.addMenu("File")
        export_action = QAction("Export Deck...", self)
        file_menu.addAction(export_action)
        self.setMenuBar(menubar)
