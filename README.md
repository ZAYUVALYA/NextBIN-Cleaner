# NextBIN

NextBIN is a system management application for Ubuntu designed to help users manage their system more easily and efficiently. It includes various features for cleaning the system, managing applications, and optimizing performance.

## 📌 Key Features

### 🔹 System Cleaner
- Removes browser cache (Firefox, Chrome, Chromium)
- Clears APT cache to free up storage space
- Deletes unnecessary thumbnail cache
- Removes old, unused kernels

### 🔹 Uninstall Manager
- Completely removes Debian applications
- Cleans up residual files after uninstallation
- Displays a list of removable applications

### 🔹 Battery Manager
- Displays real-time battery status
- Shows power consumption of each application
- Allows users to close apps that drain battery
- Power mode selection (Battery Saver, Balanced, Performance)

### 🔹 RAM Booster
- Displays real-time RAM usage
- Provides a "BOOST RAM" button to clear RAM cache

## 📖 Documentation

### **📥 Installation**
#### **1. Using the Install Script (Recommended)**
Run the following command in the terminal:
```bash
wget https://raw.githubusercontent.com/ZAYUVALYA/NextBIN-Cleaner/main/install.sh -O install.sh && chmod +x install.sh && ./install.sh
```

#### **2. Manual Installation**
```bash
sudo apt update && sudo apt install -y python3 python3-pip python3-pyqt6 python3-psutil policykit-1 power-profiles-daemon

git clone https://github.com/ZAYUVALYA/NextBIN-Cleaner.git
cd NextBIN-Cleaner
python3 src/main.py
```

### **🚀 Running NextBIN**
```bash
python3 src/main.py
```

### **🗑️ Uninstalling NextBIN**
```bash
rm -rf ~/.local/share/NextBIN
rm -f ~/.local/share/applications/nextbin.desktop
rm -f ~/.local/share/icons/hicolor/512x512/apps/NextBIN.png
update-desktop-database
```

## 🛠️ Contribution
NextBIN is still under development. If you would like to contribute, feel free to submit a pull request or report issues on the repository.

---
**NextBIN** – Clean, Manage, and Optimize Your Ubuntu System with Ease! 🚀
