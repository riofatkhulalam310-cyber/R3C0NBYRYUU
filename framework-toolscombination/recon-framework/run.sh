#!/bin/bash

# Reconnaissance Framework Quick Start Guide

echo "=========================================="
echo "Reconnaissance Framework - Quick Start"
echo "=========================================="
echo ""

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "[-] Python 3 is not installed"
    echo "[*] Please install Python 3 first"
    exit 1
fi

# Check if target is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <target>"
    echo "Example: $0 example.com"
    echo ""
    echo "Available Options:"
    echo "  $0 example.com                           # Basic scan"
    echo "  $0 example.com --mode dns                # DNS only"
    echo "  $0 example.com --mode nmap               # Nmap only"
    echo "  $0 example.com --mode full               # Full reconnaissance"
    exit 1
fi

TARGET=$1
shift
ARGS=$@

echo "[*] Target: $TARGET"
echo "[*] Starting reconnaissance framework..."
echo ""

# Run the framework
python3 main.py $TARGET $ARGS

echo ""
echo "[+] Reconnaissance completed!"
echo "[*] Check the 'output/' directory for results"
