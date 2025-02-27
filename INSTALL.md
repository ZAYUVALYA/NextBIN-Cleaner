# NextBIN Installation Guide

## 1. Automated Installation (Recommended)
For the easiest setup, use the installation script:
```bash
wget https://raw.githubusercontent.com/ZAYUVALYA/NextBIN-Cleaner/main/install.sh -O install.sh && chmod +x install.sh && ./install.sh
```
This script will:
- Install required system dependencies
- Clone the NextBIN repository
- Set up the application icon and menu shortcut
- Make NextBIN ready to use

## 2. Manual Installation
If you prefer manual installation, follow these steps:

### **Step 1: Install System Dependencies**
Run the following command to install the required packages:
```bash
sudo apt update && sudo apt install -y python3 python3-pip python3-pyqt6 python3-psutil policykit-1 tlp power-profiles-daemon
```

### **Step 2: Clone the Repository**
```bash
git clone https://github.com/ZAYUVALYA/NextBIN-Cleaner.git
cd NextBIN-Cleaner
```

### **Step 3: Run NextBIN**
```bash
python3 src/main.py
```

## 3. Uninstallation
To remove NextBIN from your system, run:
```bash
rm -rf ~/.local/share/NextBIN
rm -f ~/.local/share/applications/nextbin.desktop
rm -f ~/.local/share/icons/hicolor/512x512/apps/NextBIN.png
update-desktop-database
```
This will remove all files related to NextBIN from your system.

---

NextBIN is still in development. If you encounter any issues, please report them on GitHub! 🚀
