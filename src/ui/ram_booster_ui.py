from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QProgressBar
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt, QTimer
from core.ram_booster import RAMBooster

class RAMBoosterUI(QWidget):
    def __init__(self):
        super().__init__()
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
            QProgressBar {
                border: 2px solid #00AABB;
                border-radius: 5px;
                text-align: center;
                font-size: 14px;
            }
            QProgressBar::chunk {
                background-color: #00AABB;
            }
        """)

        layout = QVBoxLayout()
        self.setLayout(layout)

        # Title
        title_label = QLabel("RAM Booster")
        title_label.setFont(QFont("Arial", 22, QFont.Weight.Bold))
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title_label)

        # RAM Usage Progress Bar
        self.ram_progress = QProgressBar()
        self.ram_progress.setMaximum(100)
        self.ram_progress.setValue(0)
        self.ram_progress.setFormat("Loading RAM usage...")
        layout.addWidget(self.ram_progress)

        # RAM Detail Label
        self.ram_detail_label = QLabel("Total RAM: -- GB | Used RAM: -- GB")
        self.ram_detail_label.setFont(QFont("Arial", 14))
        self.ram_detail_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.ram_detail_label)

        # BOOST Button
        self.boost_button = QPushButton("BOOST RAM")
        self.boost_button.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        self.boost_button.setStyleSheet("background-color: #FFCC00; color: #121B2D;")
        self.boost_button.clicked.connect(self.boost_ram)
        layout.addWidget(self.boost_button, alignment=Qt.AlignmentFlag.AlignCenter)

        # Timer untuk real-time update RAM status setiap 2 detik
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_ram_status)
        self.timer.start(2000)  # Update setiap 2 detik

        # Panggil pertama kali
        self.update_ram_status()

    def update_ram_status(self):
        """Update status RAM secara real-time"""
        total_ram, used_ram = RAMBooster.get_ram_status()
        usage_percent = int((used_ram / total_ram) * 100)

        self.ram_progress.setValue(usage_percent)
        self.ram_progress.setFormat(f"RAM Usage: {usage_percent}%")
        self.ram_detail_label.setText(f"Total RAM: {total_ram} GB | Used RAM: {used_ram} GB")

    def boost_ram(self):
        """Jalankan RAM Booster lalu update status RAM"""
        RAMBooster.clear_cache()
        self.update_ram_status()
