# NextBIN - Ubuntu System Cleaner & Resource Manager

**Status: In Development** 🚀

NextBIN is a lightweight yet powerful system utility designed for Ubuntu-based Linux distributions. It offers essential tools for system maintenance, including cleaning cache, uninstalling applications, monitoring battery usage, and optimizing performance with a modern user interface built using **PyQt6**.

## Features (Current Limitations)
NextBIN is still in early development, so its features are currently limited. However, the following functionalities are available:

- **System Cleaner**: Remove browser cache, APT cache, thumbnail cache, and old kernels.
- **Uninstall Manager**: Easily uninstall applications along with their dependencies.
- **Battery Manager**: Monitor battery percentage, terminate high-resource processes, and switch power modes (Battery Saver, Balanced, Performance).
- **Real-time Resource Monitoring**: Similar to `htop`, track CPU, memory, and disk usage.
- **Desktop Integration**: NextBIN installs a desktop shortcut and system icon for quick access.

Future updates will expand these capabilities to include deeper system optimizations and automated cleanup processes.

---

## 🔧 Installation Guide (Ubuntu)

### **1. Automated Installation (Recommended)**
NextBIN can be installed using a simple script. Run the following command:
```bash
wget https://raw.githubusercontent.com/yourusername/NextBIN/main/install.sh -O install.sh && chmod +x install.sh && ./install.sh
```
This will automatically:
- Install required dependencies
- Clone the NextBIN repository
- Set up the application icon and menu shortcut

### **2. Manual Installation**
If you prefer manual installation, follow the steps in [INSTALL.md](INSTALL.md).

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
│── INSTALL.md               # Detailed installation instructions
│── install.sh               # Automated installation script
```

### **How to Contribute**
1. Fork the repository.
2. Create a new branch (`feature-branch-name`).
3. Commit your changes and push to your fork.
4. Open a pull request for review.

---

## 🔄 Future Updates
NextBIN is actively being developed, and upcoming features include:
- **Automated package installation** for easier setup.
- **Full Debian packaging** so it can be installed as a `.deb` package.
- **More advanced system monitoring and optimization features.**

Stay tuned for updates! 🚀
