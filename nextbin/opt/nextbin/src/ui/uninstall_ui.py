from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QListWidget, QHBoxLayout
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtCore import Qt
from core.uninstall import UninstallManager

class UninstallUI(QWidget):
    ICONS_PATH = "assets/icons/"

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Set stylesheet for elegant dark theme
        self.setStyleSheet("""
            QWidget {
                background-color: #0B192C;  /* Dark Blue Background */
                color: #F5F5F5;  /* Cream White Text */
                font-family: Arial;
            }
            QLabel {
                font-size: 16px;
            }
            QPushButton {
                background-color: #00CCDD;  /* Neon Blue for Buttons */
                color: #F5F5F5;  /* Cream White Text */
                font-size: 16px;
                padding: 10px;
                border-radius: 10px;
                border: none;
            }
            QPushButton:hover {
                background-color: #00AABB;  /* Darker Neon Blue on Hover */
            }
            QLineEdit {
                background-color: #1E2A3A;  /* Darker Blue for Input */
                color: #F5F5F5;  /* Cream White Text */
                font-size: 14px;
                padding: 10px;
                border-radius: 5px;
                border: 1px solid #00CCDD;  /* Neon Blue Border */
            }
            QListWidget {
                background-color: #1E2A3A;  /* Darker Blue for List */
                color: #F5F5F5;  /* Cream White Text */
                font-size: 14px;
                padding: 10px;
                border-radius: 5px;
                border: 1px solid #00CCDD;  /* Neon Blue Border */
            }
        """)

        layout = QVBoxLayout()
        self.setLayout(layout)

        # Application Title with Icon
        title_layout = QHBoxLayout()
        icon_label = QLabel()
        icon_label.setPixmap(QPixmap(self.ICONS_PATH + "uninstall-fill.svg").scaled(40, 40, Qt.AspectRatioMode.KeepAspectRatio))
        title_label = QLabel("Uninstall Manager")
        title_label.setFont(QFont("Arial", 20, QFont.Weight.Bold))
        title_layout.addWidget(icon_label)
        title_layout.addWidget(title_label)
        title_layout.addStretch()
        layout.addLayout(title_layout)

        # Search Bar with Icon
        search_layout = QHBoxLayout()
        search_icon_label = QLabel()
        search_icon_label.setPixmap(QPixmap(self.ICONS_PATH + "search.svg").scaled(24, 24, Qt.AspectRatioMode.KeepAspectRatio))
        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("Search for an application...")
        self.search_bar.textChanged.connect(self.search_apps)
        search_layout.addWidget(search_icon_label)
        search_layout.addWidget(self.search_bar)
        layout.addLayout(search_layout)

        # Application List
        self.app_list = QListWidget()
        layout.addWidget(self.app_list)

        # Uninstall Button with Icon
        uninstall_button_layout = QHBoxLayout()
        uninstall_icon_label = QLabel()
        uninstall_icon_label.setPixmap(QPixmap(self.ICONS_PATH + "trash-solid.svg").scaled(24, 24, Qt.AspectRatioMode.KeepAspectRatio))
        self.uninstall_button = QPushButton("Uninstall Selected App")
        self.uninstall_button.clicked.connect(self.uninstall_selected)
        uninstall_button_layout.addWidget(uninstall_icon_label)
        uninstall_button_layout.addWidget(self.uninstall_button)
        layout.addLayout(uninstall_button_layout)

        # Load list of installed applications
        self.load_installed_apps()

    def load_installed_apps(self):
        self.app_list.clear()
        installed_apps = UninstallManager.get_installed_packages()
        self.app_list.addItems(installed_apps)

    def search_apps(self):
        query = self.search_bar.text().lower()
        for i in range(self.app_list.count()):
            item = self.app_list.item(i)
            item.setHidden(query not in item.text().lower())

    def uninstall_selected(self):
        selected_item = self.app_list.currentItem()
        if selected_item:
            app_name = selected_item.text()
            UninstallManager.uninstall_package(app_name)
            self.load_installed_apps()