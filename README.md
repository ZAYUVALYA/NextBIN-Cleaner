# NextBIN - Ubuntu System Cleaner & Resource Manager

**Status: In Development** 🚀

NextBIN is a system utility application designed for Ubuntu-based Linux distributions. It provides an intuitive and powerful way to manage system resources, uninstall applications, monitor battery usage, and optimize performance with a modern user interface built using **PyQt6**.

## Features
- **System Cleaner**: Remove cache, old kernels, and unnecessary files to free up space.
- **Uninstall Manager**: Completely remove installed applications along with leftover files.
- **Battery Manager**: Monitor battery usage, terminate high-resource processes, and switch power modes (Battery Saver, Balanced, Performance).
- **Real-time Resource Monitoring**: Similar to `htop`, track CPU, memory, disk, and power usage in real time.


---

## 🔧 Installation Guide (Ubuntu)

### **1. Install Dependencies**
Before running NextBIN, install the required dependencies:
```bash
sudo apt update && sudo apt install python3 python3-pip python3-venv power-profiles-daemon tlp
```

Then, install Python dependencies:
```bash
pip install -r requirements.txt
```

### **2. Run NextBIN Manually**
Since NextBIN is still in development, you need to start it manually:
```bash
python3 src/main.py
```

This will launch the NextBIN UI, allowing you to use the cleaner, uninstall manager, and battery monitoring features.

---

## 🛠 Development & Contribution
NextBIN is an open-source project, and contributions are welcome! The project structure is as follows:
```
NextBIN/
│── src/
│   │── main.py              # Main entry point
│   │── ui/                  # UI components
│   │   │── main_window.py   # Main application window
│   │   │── cleaner_ui.py    # UI for Cleaner
│   │   │── uninstall_ui.py  # UI for Uninstall Manager
│   │   │── battery_ui.py    # UI for Battery Manager
│   │── core/                # Core logic and backend processing
│   │   │── cleaner.py       # Cleaning system logic
│   │   │── uninstall.py     # Uninstall manager logic
│   │   │── battery.py       # Battery monitoring and task management
│   │── assets/              # Icons and other assets
│
│── debian/                  # Debian package setup (WIP)
│── docs/                    # Documentation
│── tests/                   # Unit tests
│── .gitignore               # Git ignore list
│── requirements.txt         # Python dependencies
│── README.md                # Project documentation
```

### **How to Contribute**
1. Fork the repository.
2. Create a new branch (`feature-branch-name`).
3. Commit your changes and push to your fork.
4. Open a pull request for review.

---

## 🔄 Future Updates
NextBIN is actively being developed, and future updates will include:
- **Automated package installation** for easier setup.
- **Full Debian packaging** so it can be installed as a `.deb` package.
- **More advanced system monitoring and optimization features**.

Stay tuned for updates! 🚀

