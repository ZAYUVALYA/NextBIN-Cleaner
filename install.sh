#!/bin/bash

set -e  # Stop execution if any command fails

# Define installation paths
INSTALL_DIR="$HOME/.local/share/NextBIN"
DESKTOP_FILE="$HOME/.local/share/applications/nextbin.desktop"
ICON_DIR="$HOME/.local/share/icons/hicolor/512x512/apps"
ICON_FILE="$ICON_DIR/NextBIN.png"

# Step 1: Install dependencies (only power-profiles-daemon, removing tlp to avoid conflicts)
echo "Installing dependencies..."
sudo apt update
sudo apt install -y python3 python3-pip python3-pyqt6 python3-psutil policykit-1 power-profiles-daemon

# Step 2: Clone NextBIN repository
echo "Cloning NextBIN..."
rm -rf "$INSTALL_DIR"  # Remove existing installation if any
git clone https://github.com/ZAYUVALYA/NextBIN-Cleaner.git "$INSTALL_DIR"

# Step 3: Set up desktop entry and icon
echo "Setting up desktop shortcut..."
mkdir -p "$ICON_DIR"
cp "$INSTALL_DIR/NextBIN.png" "$ICON_FILE"

cat > "$DESKTOP_FILE" <<EOL
[Desktop Entry]
Version=1.0
Type=Application
Name=NextBIN
Comment=Ubuntu System Cleaner & Resource Manager
Exec=python3 $INSTALL_DIR/src/main.py
Icon=NextBIN
Terminal=false
Categories=Utility;System;
StartupNotify=true
EOL

chmod +x "$DESKTOP_FILE"
update-desktop-database

echo "NextBIN installation completed! You can find it in your application menu or run 'python3 $INSTALL_DIR/src/main.py'."
