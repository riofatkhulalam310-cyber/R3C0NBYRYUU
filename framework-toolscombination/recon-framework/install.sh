#!/bin/bash

# Reconnaissance Framework Installation Script
# For Kali Linux

echo "[*] Installing Reconnaissance Framework Dependencies..."

# Update package list
sudo apt-get update

# Install required tools
echo "[*] Installing nmap..."
sudo apt-get install -y nmap

echo "[*] Installing dnsutils (dig, nslookup)..."
sudo apt-get install -y dnsutils

echo "[*] Installing theHarvester..."
sudo apt-get install -y theHarvester

echo "[*] Installing Amass..."
sudo apt-get install -y amass

echo "[*] Installing Gobuster..."
sudo apt-get install -y gobuster

# Install Python dependencies
echo "[*] Installing Python dependencies..."
sudo apt-get install -y python3-pip

pip3 install -r requirements.txt

echo "[+] Installation completed!"
echo "[*] You can now run the framework:"
echo "    python3 main.py <target> --mode full"
