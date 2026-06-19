# QUICK REFERENCE

## Installation

```bash
cd recon-framework
sudo ./install.sh
```

## Basic Usage

```bash
# Help
python3 main.py --help

# Full reconnaissance
python3 main.py example.com --mode full

# Specific tools
python3 main.py example.com --mode dns
python3 main.py example.com --mode nmap
python3 main.py example.com --mode harvester
python3 main.py example.com --mode amass
python3 main.py example.com --mode gobuster
```

## Advanced Options

```bash
# Nmap with aggressive scanning
python3 main.py example.com --mode nmap --nmap-type aggressive

# Custom wordlist for Gobuster
python3 main.py example.com --mode gobuster --wordlist /path/to/wordlist.txt

# Custom output directory
python3 main.py example.com --output /tmp/recon_results
```

## Docker Usage

```bash
# Build Docker image
./docker-build.sh

# Run in Docker
./docker-run.sh example.com --mode full
```

## Generate HTML Report

```bash
python3 report_generator.py output/recon_example.com_*.json
```

## File Structure

- `main.py` - Main framework
- `modules/` - Tool wrappers
- `config/config.ini` - Configuration
- `output/` - Results
- `README.md` - Full documentation
- `requirements.txt` - Dependencies

## Tools Included

1. **Nmap** - Port scanning & service detection
2. **dig/nslookup** - DNS enumeration
3. **TheHarvester** - Email & subdomain discovery
4. **Amass** - Advanced subdomain enumeration  
5. **Gobuster** - Directory & vhost enumeration

## Output Format

Results are saved as JSON:
```
output/recon_<target>_<timestamp>.json
```

Each JSON file contains results from all active modules with timestamps and command details.
