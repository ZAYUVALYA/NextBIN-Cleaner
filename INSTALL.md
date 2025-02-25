# NextBIN - Installation Guide

This guide provides detailed instructions on installing, setting up, running, and uninstalling NextBIN on Ubuntu-based Linux distributions.

---

## 🔹 System Requirements
- Ubuntu 20.04 / 22.04 / 24.04 or derivative distributions.
- At least 512MB RAM.
- Python 3 installed by default.

---

## 🔧 Step 1: Install System Dependencies
NextBIN requires some system packages to function correctly. Install them using:
```bash
sudo apt update && sudo apt install tlp power-profiles-daemon policykit-1
```
These packages ensure proper battery management and system optimization features.

---

## 📦 Step 2: Install Python Dependencies
Ensure all required Python dependencies are installed:
```bash
pip install -r requirements.txt
```
This step ensures that all required libraries, such as PyQt6 and psutil, are properly installed.

---

## 🏗 Step 3: Build and Install NextBIN
To package NextBIN as a `.deb` file and install it on your system:
```bash
make
sudo dpkg -i build/nextbin-1.0.deb
```
If there are any missing dependencies, fix them using:
```bash
sudo apt-get install -f
```
This ensures all required packages are installed and properly configured.

---

## 🚀 Step 4: Running NextBIN
Once installed, you can launch NextBIN using:
```bash
nextbin
```
If you prefer to run it manually from the source directory:
```bash
python3 src/main.py
```
This is useful for development or debugging purposes.

---

## ❌ Uninstalling NextBIN
To remove NextBIN from your system, use:
```bash
sudo dpkg --remove nextbin
```
This will remove the application but retain user data. To completely remove all NextBIN-related files, including configuration and cache, run:
```bash
sudo rm -rf /opt/nextbin
sudo rm -f /usr/bin/nextbin
```

---

## ⚙️ Important Notes
1. **Sudo Permissions:** Some features, such as cleaning APT cache and switching power modes, require administrative privileges. NextBIN will prompt for sudo access via `pkexec`.
2. **Building from Source:** If you modify the source code, you need to rebuild the `.deb` package and reinstall it.
3. **Updates:** Future improvements will include better dependency resolution and enhanced features.

Stay updated for the latest enhancements! 🚀

