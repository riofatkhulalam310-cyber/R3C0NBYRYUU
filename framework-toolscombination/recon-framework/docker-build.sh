#!/bin/bash

# Docker build script for Reconnaissance Framework

IMAGE_NAME="recon-framework"
IMAGE_TAG="latest"

echo "[*] Building Docker image: $IMAGE_NAME:$IMAGE_TAG"
docker build -t $IMAGE_NAME:$IMAGE_TAG .

echo "[+] Image built successfully!"
echo ""
echo "Usage:"
echo "  docker run -v \$(pwd)/output:/recon-framework/output $IMAGE_NAME:$IMAGE_TAG example.com"
echo "  docker run -v \$(pwd)/output:/recon-framework/output $IMAGE_NAME:$IMAGE_TAG example.com --mode dns"
echo "  docker run -v \$(pwd)/output:/recon-framework/output $IMAGE_NAME:$IMAGE_TAG example.com --mode full"
