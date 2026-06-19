#!/bin/bash

# Make all scripts executable
chmod +x recon-framework/main.py
chmod +x recon-framework/examples.py
chmod +x recon-framework/report_generator.py
chmod +x recon-framework/install.sh
chmod +x recon-framework/docker-build.sh
chmod +x recon-framework/docker-run.sh
chmod +x recon-framework/run.sh

# Make all Python files executable
chmod +x recon-framework/modules/*.py

echo "[+] All scripts are now executable"
echo ""
echo "[*] Quick Start:"
echo "    1. cd recon-framework"
echo "    2. sudo ./install.sh"
echo "    3. python3 main.py example.com --mode full"
