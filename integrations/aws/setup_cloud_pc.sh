#!/bin/bash

# ========================================================
# ☁️ The Ascension Protocol | Cloud PC Setup Script
# ========================================================
# OS: Ubuntu 22.04 LTS
# Role: Install GUI (XFCE), Chrome, and Remote Desktop
# ========================================================

echo "🟢 [1/5] Updating System..."
sudo apt update
sudo apt install -y wget tasksel

echo "🟢 [2/5] Installing XFCE Desktop (Lightweight GUI)..."
# Using Xubuntu-desktop for a complete XFCE experience
sudo DEBIAN_FRONTEND=noninteractive tasksel install xubuntu-desktop

echo "🟢 [3/5] Installing Chrome Remote Desktop..."
wget https://dl.google.com/linux/direct/chrome-remote-desktop_current_amd64.deb
sudo apt install -y ./chrome-remote-desktop_current_amd64.deb
rm ./chrome-remote-desktop_current_amd64.deb

echo "🟢 [4/5] Installing Google Chrome Browser..."
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install -y ./google-chrome-stable_current_amd64.deb
rm ./google-chrome-stable_current_amd64.deb

echo "🟢 [5/5] Configuring Session..."
# Set XFCE as the default session for Chrome Remote Desktop
bash -c 'echo "exec /usr/bin/xfce4-session" > ~/.chrome-remote-desktop-session'

# Disable LightDM to save resources (we assume headless mostly)
# sudo systemctl disable lightdm.service

echo "========================================================"
echo "🎉 Cloud PC Environment READY!"
echo "========================================================"
echo "👉 NEXT STEP:"
echo "1. On your LOCAL computer, go to: https://remotedesktop.google.com/headless"
echo "2. Click 'Begin', 'Next', 'Authorize'."
echo "3. Copy the code that looks like: DISPLAY= /opt/google/chrome-remote-desktop/start-host..."
echo "4. Paste that code HERE in this terminal and press Enter."
echo "5. Set a PIN (6 digits)."
echo "========================================================"
