from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QLabel, QHBoxLayout, QStackedWidget,
    QListWidget, QListWidgetItem, QGraphicsOpacityEffect
)
from PyQt6.QtGui import QFont, QIcon
from PyQt6.QtCore import Qt, QSize, QPropertyAnimation, QPoint, QEasingCurve
import os

from ui.cleaner_ui import CleanerUI
from ui.uninstall_ui import UninstallUI
from ui.battery_ui import BatteryUI
from ui.ram_booster_ui import RAMBoosterUI

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("NextBIN")
        self.setGeometry(100, 100, 900, 550)

        # Tambahkan efek transparansi untuk animasi Fade In
        self.effect = QGraphicsOpacityEffect(self)
        self.setGraphicsEffect(self.effect)
        self.fade_animation = QPropertyAnimation(self.effect, b"opacity")
        self.fade_animation.setDuration(500)  # Lebih cepat agar smooth
        self.fade_animation.setStartValue(0)
        self.fade_animation.setEndValue(1)
        self.fade_animation.start()

        self.init_ui()

    def init_ui(self):
        """Fungsi untuk membuat tampilan UI utama."""
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QHBoxLayout(self.central_widget)

        # Sidebar Navigasi
        self.sidebar = QListWidget()
        self.sidebar.setFixedWidth(220)  # Sedikit lebih lebar agar lebih proporsional
        self.sidebar.setStyleSheet("""
            QListWidget {
                background-color: #1E2A38;  /* Warna lebih soft */
                border: none;
                color: white;
                font-size: 16px;
                padding: 10px;
            }
            QListWidget::item {
                padding: 12px;
                border-radius: 5px;
            }
            QListWidget::item:selected {
                background-color: #00CCDD;
            }
        """)

        # Tambahkan ikon sidebar
        icons_path = os.path.abspath("NextBIN.png")
        self.setWindowIcon(QIcon(icons_path))

        menu_items = [
        ("Cleaner", "assets/icons/trash-solid.svg"),
        ("Uninstall Manager", "assets/icons/uninstall-fill.svg"),
        ("Battery Manager", "assets/icons/battery-full-solid.svg"),
        ("RAM Booster", "assets/icons/computer-solid.svg"),
    ]


        for name, icon in menu_items:
            item = QListWidgetItem(QIcon(icon), name)
            self.sidebar.addItem(item)

        self.layout.addWidget(self.sidebar)

        # Stacked Widget untuk Konten
        self.stack = QStackedWidget()
        self.cleaner_ui = CleanerUI()
        self.uninstall_ui = UninstallUI()
        self.battery_ui = BatteryUI()
        self.ram_booster_ui = RAMBoosterUI()

        self.stack.addWidget(self.cleaner_ui)
        self.stack.addWidget(self.uninstall_ui)
        self.stack.addWidget(self.battery_ui)
        self.stack.addWidget(self.ram_booster_ui)

        self.layout.addWidget(self.stack)

        # Animasi Sidebar (Perbaikan Bug)
        self.sidebar.move(-220, 0)  # Sidebar mulai dari luar layar
        self.sidebar_animation = QPropertyAnimation(self.sidebar, b"pos")
        self.sidebar_animation.setDuration(600)
        self.sidebar_animation.setStartValue(QPoint(-220, 0))
        self.sidebar_animation.setEndValue(QPoint(0, 0))
        self.sidebar_animation.setEasingCurve(QEasingCurve.Type.OutCubic)
        self.sidebar_animation.start()

        # Hubungkan sidebar ke fungsi perubahan halaman
        self.sidebar.currentRowChanged.connect(self.switch_page)
        self.sidebar.setCurrentRow(0)
        self.stack.setCurrentWidget(self.cleaner_ui)

    def switch_page(self, index):
        """Ganti halaman berdasarkan pilihan di sidebar."""
        self.stack.setCurrentIndex(index)
