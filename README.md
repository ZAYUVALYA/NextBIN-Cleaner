# NextBIN

NextBIN is an advanced system management tool designed specifically for Ubuntu. It provides powerful utilities to optimize, clean, and manage your system efficiently. With a modern interface and real-time monitoring, NextBIN helps users maintain peak system performance effortlessly.

## 🚀 Features

### 🧹 System Cleaner
- **Browser Cache Cleanup**: Removes cached data from Firefox, Chrome, and Chromium.
- **APT Cache Cleanup**: Clears package manager cache to free up disk space.
- **Thumbnail Cache Cleanup**: Deletes unnecessary thumbnails from the system.
- **Old Kernel Removal**: Identifies and removes outdated Linux kernels.

### 🗑️ Uninstall Manager
- **Complete Debian Package Removal**: Uninstalls applications along with their dependencies.
- **Residual File Cleanup**: Eliminates leftover files after uninstallation.
- **Application List Display**: Provides a list of installed applications for easy management.

### 🔋 Battery Manager
- **Real-time Battery Status**: Monitors current battery level and usage.
- **Per-App Power Consumption**: Displays power usage for each running application.
- **End Task Functionality**: Allows force-closing battery-draining apps.
- **Power Mode Selection**: Switch between Battery Saver, Balanced, and Performance modes.

### 🚀 RAM Booster
- **Live RAM Usage Monitoring**: Tracks memory consumption in real time.
- **Memory Optimization**: Provides a "BOOST RAM" button to clear unnecessary memory usage.

## 📖 Documentation
For detailed installation instructions, usage, and troubleshooting, refer to [INSTALL.md](INSTALL.md).

## 🛠️ Development
### 🔹 Tech Stack
NextBIN is built using the following technologies:
- **Python 3** – Core logic and system management.
- **PyQt6** – Modern UI framework for the graphical interface.
- **psutil** – System monitoring for CPU, RAM, and battery.
- **policykit-1** – For handling system-level permissions securely.

### 🔹 Project Structure
```
NextBIN/
│── src/                     # Source code directory
│   │── main.py              # Main application entry point
│   │── ui/                  # UI components
│   │   │── main_window.py   # Main window layout
│   │   │── cleaner_ui.py    # Cleaner interface
│   │   │── uninstall_ui.py  # Uninstall manager interface
│   │   │── battery_ui.py    # Battery manager interface
│   │   │── ram_booster_ui.py # RAM booster interface
│   │── core/                # Core system functionalities
│   │   │── cleaner.py       # System cleaner logic
│   │   │── uninstall.py     # Uninstall manager logic
│   │   │── battery.py       # Battery management logic
│   │   │── ram_booster.py   # RAM management logic
│   │── assets/              # Icons and styling assets
│
│── LICENSE                  # Project license
│── README.md                # Project documentation
│── INSTALL.md               # Installation guide
│── requirements.txt         # Dependencies list
│── install.sh               # Install script
│── NextBIN.png              # Application logo
```

## 🔧 Contribution
Contributions are welcome! If you’d like to improve NextBIN, feel free to:
- **Submit Issues**: Report bugs or request features via GitHub Issues.
- **Fork & Pull Requests**: Implement new features or fix bugs and submit a pull request.
- **Enhance Documentation**: Improve existing docs for better clarity.

## ⚖️ License
NextBIN is released under the **MIT License**. See [LICENSE](LICENSE) for more details.

---
**NextBIN – Optimize, Clean, and Manage Your Ubuntu System Efficiently! 🚀**
