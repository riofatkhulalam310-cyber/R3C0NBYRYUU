# Installation Guide

Complete step-by-step installation guide for the Reconnaissance Framework.

## Table of Contents

- [System Requirements](#system-requirements)
- [Prerequisites](#prerequisites)
- [Installation Methods](#installation-methods)
- [Verification](#verification)
- [Troubleshooting](#troubleshooting)
- [Next Steps](#next-steps)

---

## System Requirements

### Minimum
- **OS**: Kali Linux 2023+ or Debian 11+
- **Python**: 3.7+
- **RAM**: 2GB
- **Disk Space**: 500MB
- **Internet**: Required

### Recommended
- **OS**: Kali Linux 2024
- **Python**: 3.10+
- **RAM**: 4GB+
- **Disk Space**: 1GB+
- **Network**: Stable internet connection

### Supported Platforms

| Platform | Status | Notes |
|----------|--------|-------|
| Kali Linux | ✅ Supported | Recommended |
| Ubuntu 22.04 LTS | ✅ Supported | Tested |
| Debian 11+ | ✅ Supported | Tested |
| Parrot Security | ✅ Supported | Compatible |
| Windows (WSL2) | ⚠️ Limited | Use Kali Linux WSL |
| macOS | ⚠️ Limited | Most tools available |
| Docker | ✅ Supported | Recommended alternative |

---

## Prerequisites

### 1. Update System

```bash
# Update package lists
sudo apt-get update

# Upgrade installed packages (optional but recommended)
sudo apt-get upgrade -y

# Install essential build tools
sudo apt-get install -y build-essential
```

### 2. Check Python Installation

```bash
# Check if Python 3 is installed
python3 --version

# If not installed:
sudo apt-get install -y python3 python3-pip python3-venv
```

### 3. Install Git (Optional, for cloning)

```bash
sudo apt-get install -y git
```

---

## Installation Methods

### Method 1: Automated Installation (Recommended)

**Best for**: Quick setup, ensures all dependencies installed

```bash
# Navigate to framework directory
cd recon-framework

# Make install script executable
chmod +x install.sh

# Run automated installation
sudo ./install.sh

# Wait for installation to complete
# This will install all tools and Python dependencies
```

**What it does:**
- Updates package list
- Installs nmap
- Installs dnsutils (dig, nslookup)
- Installs theHarvester
- Installs amass
- Installs gobuster
- Installs Python dependencies

**Time required**: 10-15 minutes

---

### Method 2: Manual Installation

**Best for**: Understanding each step, custom configurations

#### Step 1: Install System Packages

```bash
# Update packages
sudo apt-get update

# Install each tool
sudo apt-get install -y nmap
sudo apt-get install -y dnsutils
sudo apt-get install -y theHarvester
sudo apt-get install -y amass
sudo apt-get install -y gobuster

# Install Python development packages
sudo apt-get install -y python3-dev python3-pip
```

#### Step 2: Install Python Dependencies

```bash
# Navigate to framework directory
cd recon-framework

# Install Python packages
pip3 install -r requirements.txt
```

#### Step 3: Make Scripts Executable

```bash
# Make Python scripts executable
chmod +x main.py
chmod +x examples.py
chmod +x report_generator.py
chmod +x run.sh

# Make module scripts executable
chmod +x modules/*.py
```

**Time required**: 15-20 minutes

---

### Method 3: Docker Installation

**Best for**: Clean environment, cross-platform compatibility, no local conflicts

#### Step 1: Install Docker

```bash
# On Kali Linux
sudo apt-get install -y docker.io

# Start Docker service
sudo systemctl start docker

# Add user to docker group (optional)
sudo usermod -aG docker $USER
newgrp docker

# Verify Docker installation
docker --version
```

#### Step 2: Build Docker Image

```bash
# Navigate to framework directory
cd recon-framework

# Make build script executable
chmod +x docker-build.sh

# Build Docker image
./docker-build.sh

# Or build manually
docker build -t recon-framework:latest .
```

**Time required**: 5-10 minutes (download and build)

#### Step 3: Test Docker Installation

```bash
# Test Docker image
docker run recon-framework:latest --help
```

**Time required**: Docker usage

---

### Method 4: Virtual Environment Installation

**Best for**: Isolation from system Python, multiple versions

```bash
# Navigate to framework directory
cd recon-framework

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run framework
python3 main.py example.com

# Deactivate when done
deactivate
```

---

## Verification

### 1. Verify System Tools

```bash
# Check each tool is installed
which nmap
which dig
which nslookup
which theHarvester
which amass
which gobuster

# Get version information
nmap --version
dig -v
theHarvester -h | head -5
amass --version
gobuster version
```

**Expected output**: Version numbers and installation paths

### 2. Verify Python Installation

```bash
# Check Python version (should be 3.7+)
python3 --version

# Check pip installation
pip3 --version

# Verify package installation
python3 -c "import subprocess; print('OK')"
```

### 3. Test Framework

```bash
# Navigate to framework
cd recon-framework

# Test framework help
python3 main.py --help

# Expected output: Help message with usage information
```

### 4. Run Test Scan

```bash
# Run a test scan (may need sudo for nmap)
python3 main.py example.com --mode dns

# Check output
ls -lah output/

# View results
cat output/recon_example.com_*.json | jq '.'
```

---

## Installation Verification Checklist

```
☐ Python 3.7+ installed
☐ nmap installed and working
☐ dig/nslookup available
☐ theHarvester installed
☐ amass installed
☐ gobuster installed
☐ Framework directory accessible
☐ requirements.txt installed
☐ main.py executable
☐ Help command works: python3 main.py --help
☐ Test DNS scan completes: python3 main.py example.com --mode dns
☐ Output directory created
☐ Results in JSON format
```

---

## Troubleshooting Installation

### Issue: "Command not found: nmap"

**Solution:**
```bash
# Install nmap
sudo apt-get install -y nmap

# Verify
which nmap
nmap --version
```

### Issue: "ModuleNotFoundError: No module named 'subprocess'"

**Solution:**
```bash
# This module is built-in, check Python installation
python3 -c "import subprocess; print('OK')"

# If still failing, reinstall Python
sudo apt-get install --reinstall python3
```

### Issue: "Permission denied" when running nmap

**Solution:**
```bash
# Use sudo for nmap scans
sudo python3 main.py example.com --mode nmap

# Or make nmap setuid (not recommended for security)
# Instead, use sudo for the framework
```

### Issue: "pip3: command not found"

**Solution:**
```bash
# Install pip
sudo apt-get install -y python3-pip

# Verify
pip3 --version

# Install dependencies
pip3 install -r requirements.txt
```

### Issue: "Locale not installed" warning

**Solution:**
```bash
# Fix locale settings
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8

# Or permanently:
echo "export LC_ALL=en_US.UTF-8" >> ~/.bashrc
echo "export LANG=en_US.UTF-8" >> ~/.bashrc
source ~/.bashrc
```

### Issue: Installation hangs or times out

**Solution:**
```bash
# Check internet connection
ping 8.8.8.8

# Try installing one tool at a time
sudo apt-get install nmap
# Wait for completion
sudo apt-get install dnsutils
# Etc.

# Or retry with timeout
timeout 600 sudo apt-get install -y nmap
```

### Issue: Disk space error

**Solution:**
```bash
# Check available space
df -h

# Clean apt cache
sudo apt-get clean
sudo apt-get autoclean

# Remove old packages
sudo apt-get autoremove

# If still insufficient, expand disk or use Docker
```

---

## Post-Installation Setup

### 1. Configure Framework

```bash
# Edit configuration file
nano config/config.ini

# Customize settings as needed
# Set timeouts, enable/disable tools, etc.
```

### 2. Set Up Wordlists

```bash
# Verify wordlist location
ls /usr/share/wordlists/dirb/

# Or download SecLists
git clone https://github.com/danielmiessler/SecLists.git wordlists
```

### 3. Create Output Directory

```bash
# Framework creates this automatically, but verify
mkdir -p output

# Set permissions
chmod 755 output
```

### 4. Test All Modules

```bash
# Run individual module tests
python3 main.py example.com --mode dns
python3 main.py example.com --mode nmap
python3 main.py example.com --mode harvester
python3 main.py example.com --mode amass
python3 main.py main.py example.com --mode gobuster
```

---

## Uninstallation

### Remove Framework

```bash
# Navigate to parent directory
cd ..

# Remove framework directory
rm -rf recon-framework

# Remove installed tools (optional)
sudo apt-get remove -y nmap dnsutils theHarvester amass gobuster

# Remove Python dependencies
pip3 uninstall -r requirements.txt -y
```

### Docker Cleanup

```bash
# Remove Docker image
docker rmi recon-framework:latest

# Remove container
docker rm <container_id>

# Clean up Docker
docker system prune -a
```

---

## Next Steps

After successful installation:

1. **Read Documentation**
   - [README.md](README.md) - Overview and usage
   - [FRAMEWORK_STRUCTURE.md](FRAMEWORK_STRUCTURE.md) - Architecture details
   - [QUICK_REFERENCE.md](QUICK_REFERENCE.md) - Command reference

2. **Run First Scan**
   ```bash
   python3 main.py example.com --mode full
   ```

3. **Explore Results**
   ```bash
   cat output/recon_*.json | jq '.'
   ```

4. **Generate HTML Report**
   ```bash
   python3 report_generator.py output/recon_*.json
   ```

5. **Read FAQ**
   - [FAQ.md](FAQ.md) - Common questions and answers

6. **Get Help**
   - Check [CONTRIBUTING.md](CONTRIBUTING.md) for support options
   - Open GitHub issues for problems
   - Review [SECURITY.md](SECURITY.md) for security guidelines

---

## System-Specific Instructions

### Kali Linux

```bash
# Most compatible
sudo apt-get update
sudo apt-get install -y kali-tools-reconnaissance
# Then follow Method 1 or 2
```

### Ubuntu 22.04

```bash
# Enable universe repository
sudo add-apt-repository universe

# Then proceed with installation methods
```

### Debian 11

```bash
# Enable backports for newer tools
echo "deb http://deb.debian.org/debian bullseye-backports main" | sudo tee /etc/apt/sources.list.d/backports.list

# Update and install
sudo apt-get update
sudo apt-get install -y -t bullseye-backports gobuster
```

### Docker (Any System)

```bash
# Use Docker method which works on any system with Docker
./docker-build.sh
./docker-run.sh example.com --mode full
```

---

## Security Considerations

### File Permissions

```bash
# Restrict framework directory
chmod 755 recon-framework

# Protect output files
chmod 600 output/recon_*.json

# Protect configuration
chmod 600 config/config.ini
```

### Keep Tools Updated

```bash
# Regular updates
sudo apt-get update
sudo apt-get upgrade -y

# Check for security updates
sudo apt list --upgradable
```

### Secure Credentials

```bash
# Never hardcode API keys
# Use environment variables instead
export SHODAN_API_KEY="your-key"

# Or create .env file (not in git)
echo "SHODAN_API_KEY=your-key" > .env
```

---

## Getting Help

- 📖 Documentation: See README.md and FRAMEWORK_STRUCTURE.md
- ❓ FAQ: Check FAQ.md for common questions
- 🐛 Issues: Report problems on GitHub
- 💬 Discussions: Join community discussions
- 📧 Email: Contact maintainers

---

**Installation Complete!**

You're now ready to start performing reconnaissance. Start with:

```bash
python3 main.py <your-target> --mode full
```

For detailed usage instructions, see [README.md](README.md).

---

**Last Updated**: 2024-01-01
