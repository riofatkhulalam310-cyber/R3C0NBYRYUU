# Frequently Asked Questions (FAQ)

## Installation & Setup

### Q: What are the system requirements?
**A:** 
- Kali Linux 2023+ or Debian-based Linux
- Python 3.7 or higher
- 2GB RAM minimum (4GB+ recommended)
- 500MB disk space for tools and output
- Internet connection

### Q: Can I install on Windows or macOS?
**A:**
- **Windows**: Use WSL2 (Windows Subsystem for Linux) with Kali Linux
- **macOS**: Most tools are available via Homebrew, but testing is limited
- **Recommended**: Use Docker for cross-platform compatibility

### Q: How do I install on a fresh Kali Linux?
**A:**
```bash
cd recon-framework
chmod +x install.sh
sudo ./install.sh
```

### Q: Can I use Docker instead of local installation?
**A:** Yes! Docker provides a consistent environment:
```bash
./docker-build.sh
./docker-run.sh example.com --mode full
```

### Q: What if installation fails?
**A:**
1. Check internet connection
2. Verify system packages: `which nmap dig theHarvester amass gobuster`
3. Check Python version: `python3 --version`
4. Review install.sh output for specific errors
5. Try manual installation of individual tools

---

## Usage Questions

### Q: What does the "--mode full" option do?
**A:** Runs all reconnaissance modules in sequence:
1. DNS enumeration (dig, nslookup, zone transfers)
2. Nmap port scanning (top 1000 ports)
3. TheHarvester (email and subdomain discovery)
4. Amass (advanced subdomain enumeration)
5. Gobuster (directory enumeration)

### Q: Which mode should I use for a quick scan?
**A:**
```bash
# Quick DNS check
python3 main.py example.com --mode dns

# Quick port scan
python3 main.py example.com --mode nmap

# For comprehensive but slightly faster: aggressive nmap + DNS
python3 main.py example.com --mode dns
python3 main.py example.com --mode nmap --nmap-type aggressive
```

### Q: Do I need sudo/root privileges?
**A:** 
- **Yes** for Nmap (raw socket access required)
- **No** for other modules individually
- **Recommended**: Use sudo for full scans

### Q: How long does a full scan take?
**A:**
- **DNS only**: 5-10 seconds
- **Nmap (basic)**: 30-60 seconds
- **Harvester**: 1-5 minutes (rate-limited)
- **Amass**: 2-10 minutes
- **Gobuster**: 5-30 minutes (depends on wordlist size)
- **Full scan**: 15-60 minutes total

### Q: Can I interrupt a scan?
**A:** Yes, press `Ctrl+C`. The current module will stop, but already completed modules won't be affected.

### Q: What if I only need one tool's results?
**A:**
```bash
# Just DNS
python3 main.py example.com --mode dns

# Just Nmap
python3 main.py example.com --mode nmap

# Just directories
python3 main.py example.com --mode gobuster
```

---

## Output & Results

### Q: Where are the results saved?
**A:** 
```
output/recon_<target>_<timestamp>.json
output/recon_<target>_<timestamp>.html (if HTML report generated)

Example:
output/recon_example.com_20240101_120000.json
```

### Q: How do I view the results?
**A:**
```bash
# View JSON results
cat output/recon_example.com_*.json | jq '.'

# View specific section
jq '.results.dns' output/recon_example.com_*.json

# Generate HTML report
python3 report_generator.py output/recon_example.com_*.json

# Open in browser
firefox output/recon_example.com_*.html
```

### Q: What format are the results in?
**A:** JSON with nested structure:
```json
{
    "target": "example.com",
    "timestamp": "20240101_120000",
    "results": {
        "dns": {...},
        "nmap": {...},
        "harvester": {...},
        "amass": {...},
        "gobuster": {...}
    }
}
```

### Q: Can I export results to CSV?
**A:**
```bash
# Simple conversion to CSV
jq -r '.results.dns.dns_records | to_entries[] | "\(.key),\(.value[])"' output/recon_*.json > results.csv

# Or use Python for advanced formatting
python3 -c "
import json, csv
with open('output/recon_example.com_*.json') as f:
    data = json.load(f)
    # Your conversion logic here
"
```

### Q: How much disk space do results use?
**A:**
- Typical full scan: 100KB - 1MB JSON
- HTML report: 50KB - 500KB
- Multiple targets: Can accumulate, consider archiving

---

## Troubleshooting

### Q: I get "Permission denied" error
**A:**
```bash
# Nmap requires root/sudo
sudo python3 main.py example.com --mode nmap

# Or run entire framework with sudo
sudo python3 main.py example.com --mode full
```

### Q: "Command not found: nmap"
**A:**
```bash
# Install missing tool
sudo apt-get install nmap

# Verify installation
which nmap
nmap --version
```

### Q: DNS returns no results
**A:**
```bash
# Check internet connection
ping 8.8.8.8

# Try manual dig command
dig @8.8.8.8 example.com

# Check if target is valid
nslookup example.com
```

### Q: TheHarvester returns empty results
**A:**
- Rate limiting may be active
- Wait 5-10 minutes and try again
- Try individual source: `theHarvester -d example.com -b google`
- Check internet connection
- Domain may not have public information

### Q: Nmap scan is very slow
**A:**
```bash
# Use basic scan instead of aggressive
python3 main.py example.com --mode nmap --nmap-type basic

# Scan fewer ports
nmap -F example.com  # Top 100 ports

# Reduce scan rate
nmap -T2 example.com  # Paranoid timing
```

### Q: "Module not found" error
**A:**
```bash
# Check Python path
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
python3 main.py example.com

# Or ensure you're in the correct directory
cd recon-framework
python3 main.py example.com
```

### Q: Wordlist not found for Gobuster
**A:**
```bash
# Find available wordlists
find /usr/share/wordlists -name "*.txt" | head -10

# Use absolute path
python3 main.py example.com --mode gobuster \
    --wordlist /usr/share/wordlists/dirb/common.txt

# Or download custom wordlist
# https://github.com/danielmiessler/SecLists
```

### Q: Error: "Address already in use"
**A:**
```bash
# Kill process using the port
sudo lsof -i :80
sudo kill -9 <PID>

# Or use different port if running web service
```

### Q: Docker build fails
**A:**
```bash
# Update Docker
docker --version

# Try building with verbose output
docker build -t recon-framework:latest --progress=plain .

# Check disk space
docker system df

# Clean up
docker system prune -a
```

---

## Performance & Optimization

### Q: How can I make scans faster?
**A:**
1. Use appropriate scan types
2. Reduce wordlist size for Gobuster
3. Skip unnecessary modules
4. Use basic instead of aggressive Nmap
5. Run scans during off-hours to avoid congestion

### Q: Can I scan multiple targets in parallel?
**A:**
```bash
# Run in background
python3 main.py target1.com --mode full &
python3 main.py target2.com --mode full &
wait  # Wait for all to complete
```

### Q: How can I reduce output file size?
**A:**
```bash
# Compress results
gzip output/recon_*.json

# Archive old results
tar -czf archive_2024_01.tar.gz output/recon_*_01_*.json
```

---

## Security & Legal

### Q: Is it legal to use this tool?
**A:**
- ✅ Legal: Authorized testing with written permission
- ✅ Legal: Educational purposes in lab environments
- ❌ Illegal: Unauthorized access to systems
- ❌ Illegal: Testing without explicit permission

### Q: How do I get authorization to test?
**A:**
1. Get written approval from system owner
2. Define scope clearly (what to test, what to avoid)
3. Specify testing timeframe
4. Agree on communication procedures
5. Keep documentation of authorization

### Q: What should I include in authorization?
**A:**
```
Scope of Work:
- Authorized targets: [list domains/IPs]
- Testing period: [start date] to [end date]
- Types of testing: Network reconnaissance, scanning

Boundaries:
- Do NOT: [list restrictions]
- Avoid testing: [critical systems, specific times]
- Contact: [emergency contact information]

Liability:
- Client assumes all risks
- Tester not liable for service disruption
- Results kept confidential
```

### Q: How do I keep results confidential?
**A:**
```bash
# Set restrictive permissions
chmod 600 output/recon_*.json

# Encrypt sensitive files
gpg --encrypt output/recon_*.json

# Use secure storage
# Avoid cloud storage for sensitive data

# Secure deletion
shred -vfz output/old_recon_*.json
```

---

## Advanced Topics

### Q: Can I customize tool parameters?
**A:** Edit `config/config.ini`:
```ini
[Nmap]
enable_os_detection = true
enable_service_detection = true

[Gobuster]
threads = 50
extensions = php,html,txt
```

### Q: How do I integrate with other tools?
**A:**
```python
# Export results for another tool
import json

with open('output/recon_*.json') as f:
    data = json.load(f)
    
# Process and export
subdomains = data['results']['amass']['subdomains']
with open('subdomains.txt', 'w') as f:
    f.write('\n'.join(subdomains))
```

### Q: Can I extend the framework with new tools?
**A:** Yes! Create a new module:
```python
# modules/new_tool.py
class NewTool:
    def __init__(self, target):
        self.target = target
    
    def scan(self):
        # Implementation here
        pass
```

Then update main.py to use it.

### Q: How do I submit results to a report?
**A:**
```bash
# Generate HTML report
python3 report_generator.py output/recon_*.json

# Include in documentation
# Export to PDF (using pandoc or similar)
# Include in presentation
```

---

## Community & Support

### Q: How do I report a bug?
**A:**
1. Check existing issues on GitHub
2. Create a new issue with:
   - Clear description
   - Steps to reproduce
   - Error messages
   - System information

### Q: How can I contribute?
**A:** See [CONTRIBUTING.md](CONTRIBUTING.md) for:
- Code style guidelines
- Pull request process
- Development setup
- Testing requirements

### Q: Where can I get help?
**A:**
- 📖 [README.md](README.md) - Main documentation
- 📋 [FRAMEWORK_STRUCTURE.md](FRAMEWORK_STRUCTURE.md) - Architecture details
- 🐛 [GitHub Issues](https://github.com/yourusername/recon-framework/issues)
- 💬 [Discussions](https://github.com/yourusername/recon-framework/discussions)

### Q: How do I stay updated?
**A:**
- ⭐ Star the repository
- 👁️ Watch for releases
- 📧 Subscribe to security alerts
- 📰 Follow changelog updates

---

## Technical Details

### Q: What Python version do I need?
**A:** Python 3.7 or higher. Check with:
```bash
python3 --version
```

### Q: Which tools are actually required?
**A:**
- **Required**: nmap, dnsutils
- **Optional**: theHarvester, amass, gobuster
  (Framework adapts if optional tools missing)

### Q: How do I check tool versions?
**A:**
```bash
nmap --version
dig -v
nslookup -version
theHarvester -h | grep version
amass --version
gobuster version
```

---

**Still have questions?**

- 📧 Email us
- 🐛 Open an issue
- 💬 Start a discussion
- 📚 Check documentation

---

**Last Updated**: 2024-01-01
