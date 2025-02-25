from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QComboBox, QTableWidget, QTableWidgetItem, QHeaderView, QHBoxLayout
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtCore import Qt, QTimer
from core.battery import BatteryManager

class BatteryUI(QWidget):
    ICONS_PATH = "assets/icons/"

    def __init__(self):
        super().__init__()
        self.init_ui()
        self.setup_timer()

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
                background-color: #00CCDD;
                color: #0B192C;
                font-size: 16px;
                padding: 10px;
                border-radius: 10px;
                border: none;
            }
            QPushButton:hover {
                background-color: #00AABB;  /* Darker Neon Blue on Hover */
            }
            QComboBox {
                background-color: #1E2A3A;  /* Darker Blue for Dropdown */
                color: #F5F5F5;  /* Cream White Text */
                font-size: 14px;
                padding: 10px;
                border-radius: 5px;
                border: 1px solid #00CCDD;  /* Neon Blue Border */
            }
            QTableWidget {
                background-color: #1E2A3A;  /* Darker Blue for Table */
                color: #F5F5F5;  /* Cream White Text */
                font-size: 14px;
                border-radius: 5px;
                border: 1px solid #00CCDD;  /* Neon Blue Border */
            }
            QHeaderView::section {
                background-color: #00CCDD;  /* Neon Blue for Header */
                color: #F5F5F5;  /* Cream White Text */
                padding: 10px;
                border: none;
            }
        """)

        layout = QVBoxLayout()
        self.setLayout(layout)

        # Application Title with Icon
        title_layout = QHBoxLayout()
        icon_label = QLabel()
        icon_label.setPixmap(QPixmap(self.ICONS_PATH + "battery-full-solid.svg").scaled(40, 40, Qt.AspectRatioMode.KeepAspectRatio))
        title_label = QLabel("Battery Manager")
        title_label.setFont(QFont("Arial", 20, QFont.Weight.Bold))
        title_layout.addWidget(icon_label)
        title_layout.addWidget(title_label)
        title_layout.addStretch()
        layout.addLayout(title_layout)

        # Battery Status Information
        self.battery_status_layout = QHBoxLayout()
        self.battery_icon_label = QLabel()
        self.battery_icon_label.setPixmap(QPixmap(self.ICONS_PATH + "battery-full-solid.svg").scaled(40, 40, Qt.AspectRatioMode.KeepAspectRatio))
        self.battery_status_label = QLabel("Checking battery...")
        self.battery_status_label.setFont(QFont("Arial", 16))
        self.battery_status_layout.addWidget(self.battery_icon_label)
        self.battery_status_layout.addWidget(self.battery_status_label)
        self.battery_status_layout.addStretch()
        layout.addLayout(self.battery_status_layout)

        # Dropdown for Power Plan
        self.power_plan_label = QLabel("Power Mode:")
        self.power_plan_label.setFont(QFont("Arial", 14))
        self.power_plan_dropdown = QComboBox()
        self.power_plan_dropdown.addItems(["Battery Saver", "Balanced", "Performance"])
        self.power_plan_dropdown.currentTextChanged.connect(self.change_power_plan)
        layout.addWidget(self.power_plan_label)
        layout.addWidget(self.power_plan_dropdown)

        # Table of Running Processes
        self.process_table = QTableWidget()
        self.process_table.setColumnCount(5)
        self.process_table.setHorizontalHeaderLabels(["Name", "CPU (%)", "Memory (MB)", "Disk (Bytes)", "End Task"])
        self.process_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.process_table.horizontalHeader().sectionClicked.connect(self.sort_by_column)
        layout.addWidget(self.process_table)

        # Refresh Button
        self.refresh_button = QPushButton("Refresh")
        self.refresh_button.clicked.connect(self.update_running_apps)
        layout.addWidget(self.refresh_button)

        # Update battery information and processes when the application starts
        self.update_battery_status()
        self.update_running_apps()

    def setup_timer(self):
        """Set up timer for real-time updates."""
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_running_apps)
        self.timer.start(2000)  # Update every 2 seconds

    def update_battery_status(self):
        """Update battery status."""
        battery = BatteryManager.get_battery_status()
        if battery:
            percentage = battery["percentage"]
            plugged = battery["plugged"]

            if percentage >= 90:
                icon = "battery-full-solid.svg"
            elif percentage >= 75:
                icon = "battery-three-quarters-solid.svg"
            elif percentage >= 50:
                icon = "battery-half-solid.svg"
            elif percentage >= 25:
                icon = "battery-quarter-solid.svg"
            else:
                icon = "battery-empty-solid.svg"

            self.battery_icon_label.setPixmap(QPixmap(self.ICONS_PATH + icon).scaled(40, 40, Qt.AspectRatioMode.KeepAspectRatio))
            status_text = f"Battery: {percentage}% {'(Plugged in)' if plugged else '(Discharging)'}"
        else:
            status_text = "Battery status unavailable"

        self.battery_status_label.setText(status_text)

    def update_running_apps(self):
        """Update the list of running applications."""
        # Save the column being sorted and its order
        sort_column = self.process_table.horizontalHeader().sortIndicatorSection()
        sort_order = self.process_table.horizontalHeader().sortIndicatorOrder()

        # Get data of running applications
        apps = BatteryManager.get_running_apps()

        # Update data in the table without changing row order
        for row, app in enumerate(apps):
            # If row already exists, update its items
            if row < self.process_table.rowCount():
                self.process_table.item(row, 0).setText(app['name'])
                self.process_table.item(row, 1).setText(f"{app['cpu']:.1f}")
                self.process_table.item(row, 2).setText(f"{app['memory']:.1f}")
                self.process_table.item(row, 3).setText(f"{app['disk']:,}")
            else:
                # If new row, add new row
                self.process_table.insertRow(row)
                self.process_table.setItem(row, 0, QTableWidgetItem(app['name']))
                self.process_table.setItem(row, 1, QTableWidgetItem(f"{app['cpu']:.1f}"))
                self.process_table.setItem(row, 2, QTableWidgetItem(f"{app['memory']:.1f}"))
                self.process_table.setItem(row, 3, QTableWidgetItem(f"{app['disk']:,}"))

                # Add "End Task" button
                end_task_btn = QPushButton("End Task")
                end_task_btn.setStyleSheet("background-color: #FFF100; color: #0B192C; font-size: 10px; border-radius: 0; padding 5px;")  # Yellow Button
                end_task_btn.clicked.connect(lambda _, pid=app['pid']: BatteryManager.kill_process(pid, self))
                self.process_table.setCellWidget(row, 4, end_task_btn)

        # Remove unnecessary rows (if any)
        while self.process_table.rowCount() > len(apps):
            self.process_table.removeRow(self.process_table.rowCount() - 1)

        # Restore sorting to the previously sorted column
        self.process_table.sortItems(sort_column, sort_order)

    def sort_by_column(self, index):
        """Sort the table by the clicked column."""
        self.process_table.sortItems(index, Qt.SortOrder.DescendingOrder if self.process_table.horizontalHeaderItem(index).text().endswith("↓") else Qt.SortOrder.AscendingOrder)
        
        # Update header text to indicate sorting direction
        for i in range(self.process_table.columnCount()):
            text = self.process_table.horizontalHeaderItem(i).text().rstrip("↓↑")
            self.process_table.horizontalHeaderItem(i).setText(f"{text} {'↓' if i == index else '↑'}")

    def change_power_plan(self, mode):
        """Change the power mode according to the user's choice."""
        BatteryManager.set_power_plan(mode)