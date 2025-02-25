from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QProgressBar, QStackedWidget
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt, QTimer
import psutil
from ui.cleaner_ui import CleanerUI
from ui.uninstall_ui import UninstallUI
from ui.battery_ui import BatteryUI

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("NextBIN")
        self.setGeometry(100, 100, 800, 500)
        self.setStyleSheet("background-color: #3B82F6; color: white; font-family: Arial;")
        
        # Main Widget
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Header
        self.header_layout = QHBoxLayout()
        self.time_label = QLabel("NextBIN - System Management")
        self.time_label.setFont(QFont("Arial", 12))
        self.header_layout.addWidget(self.time_label)
        self.layout.addLayout(self.header_layout)

        # Stacked Widget (For Different Pages)
        self.stack = QStackedWidget()
        self.cleaner_ui = CleanerUI()
        self.uninstall_ui = UninstallUI()
        self.battery_ui = BatteryUI()

        self.stack.addWidget(self.cleaner_ui)
        self.stack.addWidget(self.uninstall_ui)
        self.stack.addWidget(self.battery_ui)
        self.layout.addWidget(self.stack)

        # Navigation Buttons
        self.nav_layout = QHBoxLayout()

        self.nav_cleaner = QPushButton("Cleaner")
        self.nav_cleaner.clicked.connect(lambda: self.stack.setCurrentWidget(self.cleaner_ui))
        self.nav_uninstall = QPushButton("Uninstall Manager")
        self.nav_uninstall.clicked.connect(lambda: self.stack.setCurrentWidget(self.uninstall_ui))
        self.nav_battery = QPushButton("Battery Manager")
        self.nav_battery.clicked.connect(lambda: self.stack.setCurrentWidget(self.battery_ui))
        
        self.nav_layout.addWidget(self.nav_cleaner)
        self.nav_layout.addWidget(self.nav_uninstall)
        self.nav_layout.addWidget(self.nav_battery)
        self.layout.addLayout(self.nav_layout)
        
        # Display the Cleaner Page by Default
        self.stack.setCurrentWidget(self.cleaner_ui)
