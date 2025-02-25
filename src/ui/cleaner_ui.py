from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QCheckBox
from core.cleaner import Cleaner

class CleanerUI(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.setStyleSheet("background-color: #3B82F6; color: white; font-family: Arial;")

        self.title_label = QLabel("CLEANER")
        self.title_label.setStyleSheet("font-size: 24px; font-weight: bold;")
        layout.addWidget(self.title_label)

        self.cache_label = QLabel("Checking storage...")
        self.kernel_label = QLabel("Checking old kernels...")
        layout.addWidget(self.cache_label)
        layout.addWidget(self.kernel_label)

        # Checkboxes
        self.cb_browser_cache = QCheckBox("Clear Browser Cache")
        self.cb_apt_cache = QCheckBox("Clear APT Cache")
        self.cb_thumbnail_cache = QCheckBox("Clear Thumbnail Cache")
        self.cb_old_kernels = QCheckBox("Remove Old Kernels")

        for cb in [self.cb_browser_cache, self.cb_apt_cache, self.cb_thumbnail_cache, self.cb_old_kernels]:
            cb.setStyleSheet("font-size: 16px;")
            layout.addWidget(cb)

        # BOOST Button
        self.boost_button = QPushButton("BOOST")
        self.boost_button.setStyleSheet("background-color: #2563EB; color: white; font-size: 18px; padding: 10px; border-radius: 20px;")
        self.boost_button.clicked.connect(self.clean_selected)
        layout.addWidget(self.boost_button)

        self.setLayout(layout)
        self.update_cleanable_sizes()

    def update_cleanable_sizes(self):
        """Update UI dengan ukuran cache yang bisa dibersihkan."""
        sizes = Cleaner.get_cleanable_sizes()
        self.cache_label.setText(f"Cache: {sizes['browser_cache']} MB | APT: {sizes['apt_cache']} MB | Thumbnails: {sizes['thumbnail_cache']} MB")
        self.kernel_label.setText(f"Old Kernels: {sizes['old_kernels']} MB")

    def clean_selected(self):
        """Menjalankan pembersihan berdasarkan pilihan user."""
        options = {
            "browser_cache": self.cb_browser_cache.isChecked(),
            "apt_cache": self.cb_apt_cache.isChecked(),
            "thumbnail_cache": self.cb_thumbnail_cache.isChecked(),
            "old_kernels": self.cb_old_kernels.isChecked()
        }
        Cleaner.clean_selected(options)
        self.update_cleanable_sizes()
