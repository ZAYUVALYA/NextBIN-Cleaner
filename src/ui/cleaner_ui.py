from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QCheckBox, QHBoxLayout, QGridLayout, QProgressBar
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtCore import Qt
from core.cleaner import Cleaner

class CleanerUI(QWidget):
    ICONS_PATH = "assets/icons/"

    def __init__(self):
        super().__init__()
        self.checkboxes = {}  # Menyimpan referensi checkbox
        self.init_ui()

    def init_ui(self):
        # Set modern stylesheet
        self.setStyleSheet("""
            QWidget {
                background-color: #121B2D;  /* Dark background */
                color: #F5F5F5;
                font-family: Arial;
            }
            QLabel {
                font-size: 16px;
            }
            QPushButton {
                background-color: #00AABB;
                color: white;
                font-size: 16px;
                padding: 12px;
                border-radius: 8px;
                border: none;
            }
            QPushButton:hover {
                background-color: #008899;
            }
            QCheckBox {
                font-size: 14px;
                color: #F5F5F5;
                padding: 5px;
            }
            QProgressBar {
                border: 2px solid #00AABB;
                border-radius: 5px;
                text-align: center;
            }
            QProgressBar::chunk {
                background-color: #00AABB;
            }
        """)

        layout = QVBoxLayout()
        self.setLayout(layout)

        # Title
        title_label = QLabel("System Cleaner")
        title_label.setFont(QFont("Arial", 22, QFont.Weight.Bold))
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title_label)

        # Progress Bar for Cache Size
        self.cache_progress = QProgressBar()
        self.cache_progress.setMaximum(100)
        self.cache_progress.setValue(0)
        self.cache_progress.setFormat("Scanning...")
        layout.addWidget(self.cache_progress)

        # Grid Layout for Cleaning Options
        grid_layout = QGridLayout()

        self.checkboxes["browser_cache"], cb1 = self.create_checkbox_with_icon("Clear Browser Cache", "browser.svg")
        self.checkboxes["apt_cache"], cb2 = self.create_checkbox_with_icon("Clear APT Cache", "ubuntu-apt.svg")
        self.checkboxes["thumbnail_cache"], cb3 = self.create_checkbox_with_icon("Clear Thumbnail Cache", "thumbnail.svg")
        self.checkboxes["old_kernels"], cb4 = self.create_checkbox_with_icon("Remove Old Kernels", "old-karnel.svg")

        self.cb_references = [cb1, cb2, cb3, cb4]  # Menyimpan referensi agar tidak terhapus

        grid_layout.addWidget(self.checkboxes["browser_cache"], 0, 0)
        grid_layout.addWidget(self.checkboxes["apt_cache"], 0, 1)
        grid_layout.addWidget(self.checkboxes["thumbnail_cache"], 1, 0)
        grid_layout.addWidget(self.checkboxes["old_kernels"], 1, 1)

        layout.addLayout(grid_layout)

        # Clean Button
        self.clean_button = QPushButton("Clean Now")
        self.clean_button.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        self.clean_button.setStyleSheet("background-color: #FFCC00; color: #121B2D;")
        self.clean_button.clicked.connect(self.clean_selected)
        layout.addWidget(self.clean_button, alignment=Qt.AlignmentFlag.AlignCenter)

        # Update cache size information
        self.update_cleanable_sizes()

    def create_checkbox_with_icon(self, text, icon_name):
        checkbox_widget = QWidget()
        checkbox_layout = QHBoxLayout(checkbox_widget)

        # Icon
        icon_label = QLabel()
        icon_label.setPixmap(QPixmap(self.ICONS_PATH + icon_name).scaled(28, 28, Qt.AspectRatioMode.KeepAspectRatio))
        checkbox_layout.addWidget(icon_label)

        # Checkbox with Label for File Size
        checkbox = QCheckBox(f"{text} (0 B)")
        checkbox_layout.addWidget(checkbox)
        checkbox_layout.addStretch()

        return checkbox_widget, checkbox

    def update_cleanable_sizes(self):
        """Mengupdate ukuran cache yang bisa dibersihkan"""
        sizes = Cleaner.get_cleanable_sizes()

        size_labels = {
            "browser_cache": sizes['browser_cache'],
            "apt_cache": sizes['apt_cache'],
            "thumbnail_cache": sizes['thumbnail_cache'],
            "old_kernels": sizes['old_kernels']
        }

        for key, checkbox_widget in self.checkboxes.items():
            checkbox = checkbox_widget.findChild(QCheckBox)
            checkbox.setText(f"{checkbox.text().split(' (')[0]} ({self.format_size(size_labels[key])})")

        total_cache = sum(size_labels.values())
        self.cache_progress.setValue(min(100, int((total_cache / 5000) * 100)))  # Anggap 5000MB batas maksimum
        self.cache_progress.setFormat(f"Total Cleanable: {self.format_size(total_cache)}")

    def format_size(self, size_in_bytes):
        """Mengubah ukuran byte ke KB, MB, atau GB"""
        if size_in_bytes >= 1_073_741_824:
            return f"{size_in_bytes / 1_073_741_824:.2f} GB"
        elif size_in_bytes >= 1_048_576:
            return f"{size_in_bytes / 1_048_576:.2f} MB"
        elif size_in_bytes >= 1024:
            return f"{size_in_bytes / 1024:.2f} KB"
        else:
            return f"{size_in_bytes} B"

    def clean_selected(self):
        """Membersihkan cache berdasarkan opsi yang dipilih pengguna"""
        options = {
            key: checkbox.findChild(QCheckBox).isChecked()
            for key, checkbox in self.checkboxes.items()
        }
        Cleaner.clean_selected(options)
        self.update_cleanable_sizes()
