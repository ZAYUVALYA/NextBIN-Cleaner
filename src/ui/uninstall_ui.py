from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QListWidget
from core.uninstall import UninstallManager

class UninstallUI(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #3B82F6;
                color: white;
                font-family: Arial;
            }
            QPushButton {
                background-color: #2563EB;
                color: white;
                border-radius: 20px;
                padding: 10px;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #1E40AF;
            }
            QLineEdit {
                background-color: white;
                color: black;
                padding: 5px;
                border-radius: 10px;
            }
            QListWidget {
                background-color: white;
                color: black;
                border-radius: 10px;
            }
        """)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.title_label = QLabel("Uninstall Manager")
        self.layout.addWidget(self.title_label)

        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("Search for an application...")
        self.search_bar.textChanged.connect(self.search_apps)
        self.layout.addWidget(self.search_bar)

        self.app_list = QListWidget()
        self.layout.addWidget(self.app_list)

        self.uninstall_button = QPushButton("Uninstall Selected App")
        self.uninstall_button.clicked.connect(self.uninstall_selected)
        self.layout.addWidget(self.uninstall_button)

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
