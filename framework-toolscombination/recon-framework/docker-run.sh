#!/bin/bash

# Docker run script for Reconnaissance Framework

# Check if target is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <target> [additional arguments]"
    echo "Example: $0 example.com --mode full"
    exit 1
fi

IMAGE_NAME="recon-framework:latest"
TARGET=$1
shift
ARGS=$@

# Create output directory if it doesn't exist
mkdir -p output

echo "[*] Running Reconnaissance Framework on $TARGET..."
echo "[*] Output will be saved to: $(pwd)/output"
echo ""

docker run -v $(pwd)/output:/recon-framework/output \
    $IMAGE_NAME $TARGET $ARGS

echo ""
echo "[+] Reconnaissance completed!"
echo "[*] Results saved in output/ directory"
