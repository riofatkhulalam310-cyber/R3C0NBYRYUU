# 🔍 Reconnaissance Framework

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![Kali Linux](https://img.shields.io/badge/Kali%20Linux-Compatible-blue)

A comprehensive, automated reconnaissance framework that combines multiple Kali Linux security tools for efficient target enumeration and information gathering.

> **⚠️ Legal Disclaimer**: This tool is intended for authorized security testing and educational purposes only. Unauthorized access to computer systems is illegal. Always obtain proper authorization before performing any security assessments.

---

## 📋 Table of Contents

- [Features](#-features)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Quick Start](#-quick-start)
- [Usage](#-usage)
- [Architecture](#-architecture)
- [Tools Overview](#-tools-overview)
- [Output Format](#-output-format)
- [Advanced Usage](#-advanced-usage)
- [Docker Support](#-docker-support)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)

---

## ✨ Features

- **🎯 Automated Reconnaissance**: Run all reconnaissance tools with a single command
- **🔧 Modular Design**: Use individual tools or combinations as needed
- **📊 JSON Reports**: Structured output for easy parsing and analysis
- **📈 HTML Reports**: Generate beautiful HTML reports from JSON data
- **🐳 Docker Support**: Pre-configured Docker image with all tools
- **⚙️ Configurable**: Customize tool parameters via configuration files
- **🚀 Fast Execution**: Parallel processing and optimized scanning
- **💾 Result Tracking**: Timestamp-based report management
- **🔍 Multiple Reconnaissance Modes**: DNS, Nmap, Harvester, Amass, Gobuster

---

## 📦 Prerequisites

### System Requirements

- **OS**: Kali Linux 2023+ (or any Debian-based Linux distro)
- **Python**: 3.7 or higher
- **RAM**: Minimum 2GB (4GB+ recommended for full scans)
- **Disk Space**: 500MB for tools + output space
- **Network**: Active internet connection

### Required Tools

The framework uses the following security tools:

- **nmap** - Network mapping and port scanning
- **dig/nslookup** - DNS enumeration utilities
- **theHarvester** - Email and subdomain discovery
- **amass** - OWASP subdomain enumeration
- **gobuster** - Directory and DNS brute forcing

---

## 🔧 Installation

### Option 1: Automated Installation (Recommended)

```bash
# Clone or download the repository
cd recon-framework

# Make install script executable
chmod +x install.sh

# Run automatic installation
sudo ./install.sh
```

### Option 2: Manual Installation

```bash
# Install system packages
sudo apt-get update
sudo apt-get install -y python3 python3-pip nmap dnsutils theHarvester amass gobuster

# Install Python dependencies
pip3 install -r requirements.txt
```

### Option 3: Docker Installation

```bash
# Build Docker image
chmod +x docker-build.sh
./docker-build.sh

# Test Docker installation
docker run recon-framework:latest --help
```

### Verify Installation

```bash
# Check all tools are installed
which nmap dig nslookup theHarvester amass gobuster

# Check Python version
python3 --version

# Test framework help
python3 main.py --help
```

---

## 🚀 Quick Start

### Basic Reconnaissance

```bash
# Simplest usage - full reconnaissance
python3 main.py example.com

# This will automatically run all available reconnaissance modules
```

### Full Reconnaissance (Recommended)

```bash
# Complete scan with all tools
python3 main.py example.com --mode full

# Output: output/recon_example.com_<timestamp>.json
```

### Specific Tool Scans

```bash
# DNS enumeration only
python3 main.py example.com --mode dns

# Nmap port scanning only
python3 main.py example.com --mode nmap

# TheHarvester email discovery only
python3 main.py example.com --mode harvester

# Amass subdomain enumeration only
python3 main.py example.com --mode amass

# Gobuster directory enumeration only
python3 main.py example.com --mode gobuster
```

---

## 📖 Usage

### Command Syntax

```bash
python3 main.py <TARGET> [OPTIONS]
```

### Positional Arguments

| Argument | Description | Example |
|----------|-------------|---------|
| `target` | Domain name or IP address | `example.com` or `192.168.1.1` |

### Optional Arguments

```
--mode {full,dns,nmap,harvester,amass,gobuster}
    Reconnaissance mode to run
    Default: full

--nmap-type {basic,aggressive,service}
    Type of Nmap scan to perform
    Default: basic

--wordlist PATH
    Custom wordlist for Gobuster
    Default: common.txt

--output DIRECTORY
    Directory to save results
    Default: output
```

### Usage Examples

#### 1. Full Reconnaissance
```bash
python3 main.py target.com --mode full
```
Runs all modules: DNS, Nmap, TheHarvester, Amass, Gobuster

#### 2. DNS-Only Enumeration
```bash
python3 main.py target.com --mode dns
```
Performs DNS lookups, zone transfers, and record enumeration

#### 3. Aggressive Nmap Scan
```bash
python3 main.py target.com --mode nmap --nmap-type aggressive
```
Full TCP/IP scan with OS detection and service enumeration

#### 4. Custom Gobuster Wordlist
```bash
python3 main.py target.com --mode gobuster --wordlist /usr/share/wordlists/dirb/big.txt
```
Directory enumeration with custom wordlist

#### 5. Custom Output Directory
```bash
python3 main.py target.com --output /tmp/recon_results
```
Save all results to custom location

#### 6. Combination: Full Recon with Aggressive Nmap
```bash
python3 main.py target.com --mode full --nmap-type aggressive
```
Full reconnaissance with aggressive Nmap scanning

---

## 🏗️ Architecture

### System Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    User Input (CLI)                     │
└─────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────┐
│              Main Framework (main.py)                   │
│            - Argument parsing                           │
│            - Module orchestration                       │
│            - Error handling                             │
└─────────────────────────────────────────────────────────┘
           ↓          ↓          ↓          ↓         ↓
    ┌──────────┬──────────┬───────────┬──────────┬─────────┐
    ↓          ↓          ↓           ↓          ↓         ↓
┌────────┐ ┌────────┐ ┌──────────┐ ┌────────┐ ┌─────────┐
│  DNS   │ │ Nmap   │ │Harvester │ │ Amass  │ │ Gobuster│
│ Tools  │ │Scanner │ │  Tools   │ │Scanner │ │ Scanner │
└────────┘ └────────┘ └──────────┘ └────────┘ └─────────┘
    ↓          ↓          ↓           ↓          ↓         ↓
┌────────┐ ┌────────┐ ┌──────────┐ ┌────────┐ ┌─────────┐
│dig/ns  │ │nmap    │ │theHarvest│ │amass   │ │gobuster │
│lookup  │ │tool    │ │  tool    │ │tool    │ │  tool   │
└────────┘ └────────┘ └──────────┘ └────────┘ └─────────┘
    ↓          ↓          ↓           ↓          ↓         ↓
└──────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────┐
│          Report Generation (JSON/HTML)                  │
└─────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────┐
│           Output Directory (timestamped)                │
└─────────────────────────────────────────────────────────┘
```

### Project Structure

```
recon-framework/
│
├── main.py                          # Framework controller
├── report_generator.py              # HTML report generation
├── examples.py                      # Interactive examples
│
├── modules/                         # Reconnaissance modules
│   ├── __init__.py
│   ├── nmap_scanner.py              # Nmap wrapper
│   ├── dns_tools.py                 # DNS enumeration
│   ├── harvester.py                 # TheHarvester wrapper
│   ├── amass_scanner.py             # Amass wrapper
│   └── gobuster_scanner.py          # Gobuster wrapper
│
├── config/                          # Configuration
│   └── config.ini                   # Settings
│
├── output/                          # Results (auto-created)
│   ├── recon_target_*.json
│   └── recon_target_*.html
│
├── install.sh                       # Installation script
├── run.sh                           # Quick run script
├── requirements.txt                 # Python dependencies
│
├── Dockerfile                       # Docker configuration
├── docker-build.sh                  # Build script
├── docker-run.sh                    # Run script
│
├── README.md                        # This file
├── FRAMEWORK_STRUCTURE.md           # Detailed structure
└── LICENSE                          # License
```

---

## 🛠️ Tools Overview

### 1. **DNS Tools** (dig, nslookup)
**Purpose**: DNS enumeration and record discovery

**Features**:
- A/AAAA record lookup
- MX (Mail Exchange) records
- NS (Nameserver) records
- TXT records (SPF, DKIM, etc.)
- CNAME resolution
- SOA records
- Zone transfer attempts
- Reverse DNS lookup

**Output**: IP addresses, DNS records, nameservers, MX records

### 2. **Nmap Scanner**
**Purpose**: Port scanning and service detection

**Scan Types**:
- **Basic**: Top 1000 ports
- **Aggressive**: Full TCP/IP with OS detection
- **Service**: Service and version detection

**Features**:
- TCP port scanning
- UDP port scanning
- Service version detection
- OS fingerprinting
- Script scanning capability

**Output**: Open ports, running services, service versions

### 3. **TheHarvester**
**Purpose**: Email and subdomain discovery

**Search Sources**:
- Google
- Bing
- LinkedIn
- Twitter
- GitHub
- And many more

**Features**:
- Email harvesting
- Subdomain enumeration
- IP discovery
- Multi-source searching

**Output**: Email addresses, subdomains, IP addresses

### 4. **Amass**
**Purpose**: Advanced subdomain enumeration

**Capabilities**:
- Subdomain discovery
- Intelligent enumeration
- DNS source integration
- Domain tracking
- IP enumeration

**Features**:
- Active reconnaissance
- Passive reconnaissance
- Machine learning integration
- Results tracking

**Output**: Subdomains, associated IPs, DNS information

### 5. **Gobuster**
**Purpose**: Directory and virtual host enumeration

**Modes**:
- Directory brute force (HTTP/HTTPS)
- Virtual host discovery
- DNS subdomain brute force

**Features**:
- Multi-threaded scanning
- Custom wordlist support
- Status code filtering
- HTTPS/SSL support

**Output**: Valid directories, status codes, virtual hosts

---

## 📊 Output Format

### JSON Report Structure

```json
{
    "target": "example.com",
    "timestamp": "20240101_120000",
    "results": {
        "dns": {
            "dig": {
                "command": "dig example.com +short",
                "output": "93.184.216.34",
                "error": null
            },
            "dns_records": {
                "A": ["93.184.216.34"],
                "MX": ["mail.example.com"],
                "NS": ["ns1.example.com", "ns2.example.com"],
                "TXT": ["v=spf1 ..."],
                "CNAME": [],
                "SOA": [...]
            }
        },
        "nmap": {
            "basic_scan": {
                "command": "nmap -p- --top-ports 1000 example.com",
                "output": "...",
                "error": null
            }
        },
        "harvester": {...},
        "amass": {...},
        "gobuster": {...}
    }
}
```

### Report Location

```
output/recon_<target>_<timestamp>.json
output/recon_<target>_<timestamp>.html (if generated)

Examples:
output/recon_example.com_20240101_120000.json
output/recon_target.org_20240115_153045.json
```

### Generate HTML Report

```bash
python3 report_generator.py output/recon_example.com_*.json
```

---

## 🚀 Advanced Usage

### Interactive Mode

```bash
python3 examples.py
# Follow the interactive menu to select scanning options
```

### Run with Sudo (Required for Nmap)

```bash
sudo python3 main.py example.com --mode full
```

### Multiple Targets (Sequential)

```bash
for target in target1.com target2.com target3.org; do
    python3 main.py $target --mode full
    sleep 5  # Delay between targets
done
```

### Filter Specific Results

```bash
# Show only discovered subdomains
grep -o '"subdomains": \[.*\]' output/recon_*.json

# Show only open ports
grep -o '"open_ports": \[.*\]' output/recon_*.json
```

### Custom Configuration

Edit `config/config.ini` to customize:

```ini
[Nmap]
enabled = true
default_scan_type = basic
enable_service_detection = true

[Gobuster]
enabled = true
threads = 50
```

---

## 🐳 Docker Support

### Build Docker Image

```bash
chmod +x docker-build.sh
./docker-build.sh
```

### Run Reconnaissance in Docker

```bash
chmod +x docker-run.sh
./docker-run.sh example.com --mode full
```

### Or Manually with Docker

```bash
# Build
docker build -t recon-framework:latest .

# Run
docker run -v $(pwd)/output:/recon-framework/output \
    recon-framework:latest example.com --mode full
```

### Docker Advantages

- ✅ No tool installation needed
- ✅ Isolated environment
- ✅ Easy to clean up
- ✅ Portable across systems
- ✅ Version control

---

## 🔧 Configuration

### config/config.ini

```ini
[General]
timeout = 300
retry_count = 3
output_format = json

[Nmap]
enabled = true
default_scan_type = basic
enable_os_detection = true
enable_service_detection = true

[DNS]
enabled = true
perform_zone_transfer = false
perform_reverse_lookup = true

[TheHarvester]
enabled = true
limit = 500
sources = google,bing,linkedin,twitter

[Amass]
enabled = true
enable_intel = true

[Gobuster]
enabled = true
default_wordlist = /usr/share/wordlists/dirb/common.txt
extensions = php,html,txt,js,css
threads = 50

[Output]
directory = output
format = json
save_raw_output = true
generate_html_report = true
```

---

## 🐛 Troubleshooting

### Common Issues and Solutions

#### 1. Permission Denied Error
```
Error: Command failed: Permission denied

Solution:
sudo python3 main.py example.com
```

#### 2. Tool Not Found
```
Error: nmap: command not found

Solution:
sudo apt-get update
sudo apt-get install nmap

# Verify installation
which nmap
```

#### 3. Timeout Errors
```
Error: Command timed out

Solution:
# Increase timeout in config.ini
# Or scan fewer ports
python3 main.py example.com --mode nmap --nmap-type basic
```

#### 4. DNS Resolution Issues
```
Error: Temporary failure in name resolution

Solution:
# Check internet connection
ping 8.8.8.8

# Check DNS configuration
cat /etc/resolv.conf

# Use specific nameserver
dig @8.8.8.8 example.com
```

#### 5. Wordlist Not Found
```
Error: Wordlist file not found

Solution:
# Find available wordlists
find /usr/share/wordlists -name "*.txt"

# Use correct path
python3 main.py example.com --mode gobuster \
    --wordlist /usr/share/wordlists/dirb/common.txt
```

#### 6. Rate Limiting
```
Issue: TheHarvester/Amass returning few results

Solution:
# Wait and retry
sleep 300  # Wait 5 minutes
python3 main.py example.com --mode harvester

# Or reduce search limits
```

### Debug Mode

```bash
# Add Python debugging
python3 -v main.py example.com

# Check framework logs
tail -f output/recon_*.json

# Verbose mode
python3 main.py example.com -v
```

### Getting Help

```bash
# Framework help
python3 main.py --help

# Tool help
python3 main.py --help
```

---

## 📝 Examples

### Example 1: Complete Target Assessment

```bash
# Run full reconnaissance on target
python3 main.py acmecorp.com --mode full

# Generate HTML report
python3 report_generator.py output/recon_acmecorp.com_*.json

# View results
cat output/recon_acmecorp.com_*.json | jq '.'
```

### Example 2: Quick Network Scan

```bash
# Only scan ports and services
python3 main.py target.com --mode nmap --nmap-type aggressive
```

### Example 3: Email Discovery

```bash
# Discover emails associated with domain
python3 main.py company.com --mode harvester
```

### Example 4: Subdomain Enumeration

```bash
# Find all subdomains
python3 main.py target.org --mode amass
```

### Example 5: Directory Discovery

```bash
# Enumerate directories with big wordlist
python3 main.py target.com --mode gobuster \
    --wordlist /usr/share/wordlists/dirb/big.txt
```

---

## 📚 Additional Resources

### Official Tool Documentation

- **Nmap**: https://nmap.org/book/
- **TheHarvester**: https://github.com/laramies/theHarvester
- **Amass**: https://github.com/OWASP/Amass
- **Gobuster**: https://github.com/OJ/gobuster

### Security Resources

- OWASP Reconnaissance: https://owasp.org/www-project-web-security-testing-guide/
- Kali Linux Tools: https://www.kali.org/tools/

### Related Projects

- Similar frameworks and tools for reconnaissance

---

## 💡 Tips and Best Practices

### Scanning Best Practices

1. **Always Get Authorization** - Ensure you have written permission before scanning
2. **Use Appropriate Scan Types** - Don't use aggressive scanning on production systems without permission
3. **Schedule Off-Peak Times** - Scan during off-hours to minimize impact
4. **Start Small** - Test with single tools before running full recon
5. **Monitor Results** - Review outputs regularly

### Performance Tips

1. **Use Specific Wordlists** - Smaller wordlists = faster scans
2. **Limit Scope** - Focus on specific domains instead of broad ranges
3. **Adjust Timeouts** - Set appropriate timeouts based on network speed
4. **Parallel Processing** - Run multiple targets sequentially
5. **Clean Output** - Archive old reports to save disk space

### Analysis Tips

1. **Cross-Reference Results** - Compare outputs from different tools
2. **Prioritize Findings** - Focus on high-value targets first
3. **Track Changes** - Compare scans over time
4. **Document Everything** - Keep detailed notes of findings
5. **Follow Up** - Investigate interesting findings further

---

## 🤝 Contributing

Contributions are welcome! Here's how to help:

### Getting Started

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Contribution Areas

- 🐛 Bug fixes
- ✨ New features
- 📚 Documentation improvements
- 🧪 Test coverage
- 💡 Performance optimization

### Development Setup

```bash
# Clone repository
git clone https://github.com/yourusername/recon-framework.git
cd recon-framework

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install development dependencies
pip3 install -r requirements.txt
```

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software...
```

---

## ⚖️ Legal Disclaimer

**IMPORTANT**: This tool is designed for authorized security testing and educational purposes only.

- ❌ **Illegal Use**: Unauthorized access to computer systems is a crime
- ✅ **Authorized Testing**: Always obtain written permission before testing
- 📋 **Compliance**: Follow all applicable laws and regulations
- 🔒 **Responsibility**: Users are solely responsible for their actions

**The authors assume no liability for misuse or damage caused by this tool.**

---

## 🙋 Support

Need help? Here are your options:

### Documentation
- Read [FRAMEWORK_STRUCTURE.md](FRAMEWORK_STRUCTURE.md) for detailed architecture
- Check [QUICK_REFERENCE.md](QUICK_REFERENCE.md) for quick commands

### Getting Help
- 📖 Check the [README](README.md) and [FAQ](#faq)
- 🐛 [Report Issues](https://github.com/yourusername/recon-framework/issues)
- 💬 [Start Discussions](https://github.com/yourusername/recon-framework/discussions)

### Contact
- 📧 Email: your-email@example.com
- 🐦 Twitter: [@yourhandle](https://twitter.com/yourhandle)
- 💼 LinkedIn: [Your Profile](https://linkedin.com/in/yourprofile)

---

## 📊 Project Stats

- **Language**: Python 3.7+
- **Tools Integrated**: 5 (Nmap, dig/nslookup, TheHarvester, Amass, Gobuster)
- **Lines of Code**: 1000+
- **Documentation**: Complete
- **Docker Support**: Yes
- **Platform**: Linux/Kali Linux

---

## 🎯 Roadmap

### Planned Features

- [ ] Multi-target scanning with queue management
- [ ] Advanced result comparison and diff tools
- [ ] Web dashboard for result visualization
- [ ] API integration for external tools
- [ ] Slack/email notifications
- [ ] Database storage (PostgreSQL/MongoDB)
- [ ] Result archival and retrieval
- [ ] Advanced filtering and search
- [ ] Custom report templates
- [ ] Scheduled scanning

---

## 🙏 Acknowledgments

- Thanks to [Nmap Project](https://nmap.org)
- Thanks to [OWASP/Amass](https://github.com/OWASP/Amass)
- Thanks to [TheHarvester](https://github.com/laramies/theHarvester)
- Thanks to [Gobuster](https://github.com/OJ/gobuster)
- Thanks to all contributors

---

## 📅 Changelog

### v1.0.0 (2024-01-01)
- ✨ Initial release
- 🎯 Full framework implementation
- 📚 Complete documentation
- 🐳 Docker support
- 📊 JSON/HTML reporting

---

**Made with ❤️ for the security community**

*Last Updated: 2024-01-01*
