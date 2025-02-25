# NextBIN - Ubuntu System Cleaner & Resource Manager

**Status: In Development** 🚀

NextBIN is a system utility for Ubuntu-based Linux distributions, designed to clean system cache, manage installed applications, and monitor battery performance with real-time resource tracking.

## Features
- **System Cleaner**: Remove cache, old kernels, and unnecessary files.
- **Uninstall Manager**: Fully remove installed applications.
- **Battery Manager**: Monitor battery usage, terminate high-resource processes, and switch power modes.
- **Real-time Resource Monitoring**: Track CPU, memory, disk, and power usage.

---

## 🔧 Installation Guide (Ubuntu)

### **1. Install System Dependencies**
```bash
sudo apt update && sudo apt install tlp power-profiles-daemon policykit-1
```

### **2. Install Python Dependencies**
```bash
pip install -r requirements.txt
```

### **3. Build and Install NextBIN**
```bash
make
sudo dpkg -i build/nextbin-1.0.deb
```
If dependencies are missing, run:
```bash
sudo apt-get install -f
```

### **4. Run NextBIN**
```bash
nextbin
```

---

## 🛠 Development & Contribution
NextBIN is open-source, and contributions are welcome. The project structure is as follows:
```
NextBIN/
│── src/                    # Source code
│   │── main.py             # Main application entry point
│   │── ui/                 # UI components
│   │── core/               # Core logic
│   │── assets/             # Icons and other assets
│── nextbin/                # Debian package directory
│   │── DEBIAN/             # Debian packaging files
│   │── usr/bin/            # Symlink for execution
│   │── opt/nextbin/        # Installed source code location
│── build/                  # Compiled .deb packages
│── debian/                 # Original Debian packaging scripts
│── docs/                   # Documentation
│── tests/                  # Unit tests
│── .gitignore              # Ignored files
│── requirements.txt        # Python dependencies
│── INSTALL.md              # System dependency guide
│── README.md               # Project documentation
│── Makefile                # Build automation
```

### **How to Contribute**
1. Fork the repository.
2. Create a new branch (`feature-branch-name`).
3. Commit your changes and push to your fork.
4. Open a pull request for review.

---

## 🔄 Future Updates
- Improved `.deb` packaging with automatic dependency resolution.
- More advanced system monitoring features.

Stay updated for the latest improvements! 🚀

