from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem, QPushButton, QHeaderView, QComboBox
from PyQt6.QtCore import Qt, QTimer
from core.battery import BatteryManager

class BatteryUI(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        
        self.battery_status = QLabel("Checking battery...")
        layout.addWidget(self.battery_status)

        # Power Plan Dropdown
        self.power_plan_label = QLabel("Power Mode:")
        self.power_plan_dropdown = QComboBox()
        self.power_plan_dropdown.addItems(["Battery Saver", "Balanced", "Performance"])
        self.power_plan_dropdown.currentTextChanged.connect(self.change_power_plan)

        layout.addWidget(self.power_plan_label)
        layout.addWidget(self.power_plan_dropdown)

        # Table for process monitoring
        self.process_table = QTableWidget()
        self.process_table.setColumnCount(5)
        self.process_table.setHorizontalHeaderLabels(["Name", "CPU (%)", "Memory (MB)", "Disk (Bytes)", "End Task"])
        self.process_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        # Sorting functionality
        self.process_table.horizontalHeader().sectionClicked.connect(self.sort_by_column)

        layout.addWidget(self.process_table)

        # Refresh Button
        self.refresh_button = QPushButton("Refresh")
        self.refresh_button.clicked.connect(self.update_running_apps)
        layout.addWidget(self.refresh_button)

        self.setLayout(layout)

        # Timer untuk Realtime Monitoring
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_running_apps)
        self.timer.timeout.connect(self.update_battery_status)
        self.timer.start(2000)  # Update setiap 2 detik agar lebih responsif

        self.update_running_apps()
        self.update_battery_status()

    def update_running_apps(self):
        """Update daftar aplikasi yang berjalan dengan informasi resource usage."""
        self.process_table.setRowCount(0)
        apps = BatteryManager.get_running_apps()

        for row, app in enumerate(apps):
            self.process_table.insertRow(row)
            self.process_table.setItem(row, 0, QTableWidgetItem(app['name']))
            self.process_table.setItem(row, 1, QTableWidgetItem(f"{app['cpu']:.1f}"))
            self.process_table.setItem(row, 2, QTableWidgetItem(f"{app['memory']:.1f}"))
            self.process_table.setItem(row, 3, QTableWidgetItem(f"{app['disk']:,}"))

            end_task_btn = QPushButton("End Task")
            end_task_btn.clicked.connect(lambda _, pid=app['pid']: BatteryManager.kill_process(pid, self))
            self.process_table.setCellWidget(row, 4, end_task_btn)

    def update_battery_status(self):
        """Update status baterai secara real-time."""
        battery = BatteryManager.get_battery_status()
        if battery:
            status_text = f"Battery: {battery['percentage']}% {'(Plugged in)' if battery['plugged'] else '(Discharging)'}"
        else:
            status_text = "Battery status unavailable"
        self.battery_status.setText(status_text)

    def sort_by_column(self, index):
        """Melakukan sorting berdasarkan kolom yang diklik."""
        self.process_table.sortItems(index, Qt.SortOrder.DescendingOrder if self.process_table.horizontalHeaderItem(index).text().endswith("↓") else Qt.SortOrder.AscendingOrder)
        
        # Update header text to indicate sorting direction
        for i in range(self.process_table.columnCount()):
            text = self.process_table.horizontalHeaderItem(i).text().rstrip("↓↑")
            self.process_table.horizontalHeaderItem(i).setText(f"{text} {'↓' if i == index else '↑'}")

    def change_power_plan(self, mode):
        """Mengubah power plan berdasarkan pilihan dropdown."""
        BatteryManager.set_power_plan(mode)
