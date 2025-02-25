from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QStackedWidget
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from ui.cleaner_ui import CleanerUI
from ui.uninstall_ui import UninstallUI
from ui.battery_ui import BatteryUI

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("NextBIN")
        self.setGeometry(100, 100, 800, 500)
        self.setStyleSheet("""
            QWidget {
                background-color: #0B192C;  /* Dark Blue Background */
                color: #F5F5F5;  /* Cream White Text */
                font-family: Arial;
            }
            QPushButton {
                background-color: #00CCDD;  /* Neon Blue for Buttons */
                color: #F5F5F5;  /* Cream White Text */
                font-size: 14px;
                padding: 10px;
                border-radius: 5px;
                border: none;
            }
            QPushButton:hover {
                background-color: #00AABB;  /* Darker Neon Blue on Hover */
            }
            QLabel {
                font-size: 18px;
            }
        """)

        # Main Widget
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Header
        self.header_label = QLabel("NextBIN - System Management")
        self.header_label.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        self.header_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.header_label)

        # Stacked Widget for Different Pages
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

        self.stack.setCurrentWidget(self.cleaner_ui)