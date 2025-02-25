from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QCheckBox, QHBoxLayout, QGridLayout
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtCore import Qt
from core.cleaner import Cleaner

class CleanerUI(QWidget):
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
            QCheckBox {
                font-size: 14px;
                color: #F5F5F5;  /* Cream White Text */
                padding: 5px;
            }
        """)

        layout = QVBoxLayout()
        self.setLayout(layout)

        # Application Title
        title_label = QLabel("Cleaner")
        title_label.setFont(QFont("Arial", 20, QFont.Weight.Bold))
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title_label)

        # Cache Size Information
        self.cache_info_label = QLabel("Checking storage...")
        self.cache_info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.cache_info_label)

        # Grid Layout for Checkboxes and Icons
        grid_layout = QGridLayout()

        # Checkboxes for Cleaning Options with Icons
        self.cb_browser_cache = self.create_checkbox_with_icon("Clear Browser Cache", "browser.svg")
        self.cb_apt_cache = self.create_checkbox_with_icon("Clear APT Cache", "ubuntu-apt.svg")
        self.cb_thumbnail_cache = self.create_checkbox_with_icon("Clear Thumbnail Cache", "thumbnail.svg")
        self.cb_old_kernels = self.create_checkbox_with_icon("Remove Old Kernels", "old-karnel.svg")

        grid_layout.addWidget(self.cb_browser_cache, 0, 0)
        grid_layout.addWidget(self.cb_apt_cache, 0, 1)
        grid_layout.addWidget(self.cb_thumbnail_cache, 1, 0)
        grid_layout.addWidget(self.cb_old_kernels, 1, 1)

        layout.addLayout(grid_layout)

        # Clean Button
        self.clean_button = QPushButton("Clean Now")
        self.clean_button.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        self.clean_button.setStyleSheet("background-color: #FFF100; color: #0B192C;")  
        self.clean_button.clicked.connect(self.clean_selected)
        layout.addWidget(self.clean_button, alignment=Qt.AlignmentFlag.AlignCenter)

        # Update cache information when the application starts
        self.update_cleanable_sizes()

    def create_checkbox_with_icon(self, text, icon_name):
        checkbox_widget = QWidget()
        checkbox_layout = QHBoxLayout(checkbox_widget)

        # Icon
        icon_label = QLabel()
        icon_label.setPixmap(QPixmap(self.ICONS_PATH + icon_name).scaled(24, 24, Qt.AspectRatioMode.KeepAspectRatio))
        checkbox_layout.addWidget(icon_label)

        # Checkbox
        checkbox = QCheckBox(text)
        checkbox_layout.addWidget(checkbox)
        checkbox_layout.addStretch()

        return checkbox_widget

    def update_cleanable_sizes(self):
        sizes = Cleaner.get_cleanable_sizes()
        self.cache_info_label.setText(
            f"Browser Cache: {sizes['browser_cache']} MB | "
            f"APT Cache: {sizes['apt_cache']} MB | "
            f"Thumbnail Cache: {sizes['thumbnail_cache']} MB | "
            f"Old Kernels: {sizes['old_kernels']} MB"
        )

    def clean_selected(self):
        options = {
            "browser_cache": self.cb_browser_cache.findChild(QCheckBox).isChecked(),
            "apt_cache": self.cb_apt_cache.findChild(QCheckBox).isChecked(),
            "thumbnail_cache": self.cb_thumbnail_cache.findChild(QCheckBox).isChecked(),
            "old_kernels": self.cb_old_kernels.findChild(QCheckBox).isChecked()
        }
        Cleaner.clean_selected(options)
        self.update_cleanable_sizes()