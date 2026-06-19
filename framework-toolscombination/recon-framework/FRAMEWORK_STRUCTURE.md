# FRAMEWORK STRUCTURE

## File Hierarchy

```
recon-framework/
│
├── main.py                    # Main framework entry point
├── modules/                   # Tool modules
│   ├── __init__.py
│   ├── nmap_scanner.py        # Nmap port scanning module
│   ├── dns_tools.py           # DNS enumeration (dig, nslookup)
│   ├── harvester.py           # TheHarvester module
│   ├── amass_scanner.py       # Amass subdomain enumeration
│   └── gobuster_scanner.py    # Gobuster directory enumeration
│
├── config/                    # Configuration files
│   └── config.ini             # Framework configuration
│
├── output/                    # Reconnaissance results (auto-created)
│
├── requirements.txt           # Python dependencies
├── README.md                  # Complete documentation
├── FRAMEWORK_STRUCTURE.md     # This file
│
├── install.sh                 # Installation script for Kali Linux
├── examples.py                # Interactive examples
├── report_generator.py        # HTML report generator
│
├── Dockerfile                 # Docker configuration
├── docker-build.sh            # Docker build script
└── docker-run.sh              # Docker run wrapper script
```

## Module Descriptions

### 1. main.py
Main framework controller that orchestrates all reconnaissance modules.

**Features:**
- Command-line interface with argparse
- Multiple reconnaissance modes
- JSON report generation
- Modular tool integration
- Error handling and logging

**Modes:**
- `full`: Run all reconnaissance tools
- `dns`: DNS enumeration only
- `nmap`: Port scanning only
- `harvester`: Email and subdomain discovery
- `amass`: Advanced subdomain enumeration
- `gobuster`: Directory and vhost enumeration

### 2. nmap_scanner.py
Wrapper for Nmap port scanning and service detection.

**Features:**
- Basic port scan
- Aggressive scanning with OS detection
- Service and version detection
- UDP scanning
- Result parsing

**Scan Types:**
- Basic: Top 1000 ports
- Aggressive: Full TCP/IP scan with OS detection
- Service: Service and version detection
- UDP: UDP port enumeration

### 3. dns_tools.py
DNS enumeration using dig and nslookup.

**Features:**
- DNS A/MX/NS/TXT/CNAME/SOA record enumeration
- Zone transfer attempts
- Reverse DNS lookup
- Result parsing and normalization
- Multiple source queries

**Queries:**
- Forward DNS lookups
- Reverse DNS lookups
- Zone transfer attempts
- Record type enumeration

### 4. harvester.py
TheHarvester wrapper for email and subdomain discovery.

**Features:**
- Multi-source email discovery
- Subdomain enumeration
- IP address discovery
- Configurable search sources
- Result parsing

**Sources:**
- Google
- Bing
- LinkedIn
- Twitter
- GitHub

### 5. amass_scanner.py
Owasp Amass wrapper for advanced subdomain enumeration.

**Features:**
- Subdomain discovery
- IP enumeration
- Intelligence gathering
- Domain tracking
- Result parsing

**Modes:**
- Enumeration
- Verbose enumeration
- Intel gathering
- Domain tracking

### 6. gobuster_scanner.py
Gobuster wrapper for directory and DNS enumeration.

**Features:**
- Directory enumeration (HTTP/HTTPS)
- Virtual host discovery
- DNS subdomain brute force
- Customizable wordlists
- Result parsing

**Modes:**
- Directory enumeration
- HTTPS directory enumeration
- Virtual host discovery
- DNS subdomain enumeration

## Configuration Files

### config/config.ini
Framework-wide configuration:
- Tool enable/disable flags
- Default parameters
- Output settings
- Scan timeouts
- Wordlist paths

## Scripts

### install.sh
Automated installation for Kali Linux dependencies and Python packages.

```bash
sudo ./install.sh
```

### examples.py
Interactive menu for running common reconnaissance scenarios.

```bash
python3 examples.py
```

### report_generator.py
Converts JSON reports to HTML format.

```bash
python3 report_generator.py output/recon_example.com_20240101_120000.json
```

### docker-build.sh
Builds Docker image with all tools pre-installed.

```bash
./docker-build.sh
```

### docker-run.sh
Wrapper for running framework in Docker container.

```bash
./docker-run.sh example.com --mode full
```

## Output Files

All reconnaissance results are saved to the `output/` directory in JSON format:

```
output/
├── recon_example.com_20240101_120000.json
├── recon_example.com_20240101_120000.html (if generated)
├── recon_target.org_20240101_150000.json
└── ...
```

JSON Report Structure:
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

## Data Flow

```
User Input (CLI)
       ↓
  main.py (Framework Controller)
       ↓
  ┌─────────┬──────────┬──────────┬──────────┬──────────┐
  ↓         ↓          ↓          ↓          ↓          ↓
 DNS      Nmap     Harvester   Amass    Gobuster   Output
Tools    Scanner   Tools      Scanner   Scanner    Reports
  ↓         ↓          ↓          ↓          ↓          ↓
 dig/ns   nmap        th         amass     gobuster   JSON/HTML
lookup                                                 
  ↓         ↓          ↓          ↓          ↓          ↓
  └─────────┴──────────┴──────────┴──────────┴──────────┘
              ↓
        JSON Report Generation
              ↓
        HTML Report (Optional)
```

## Integration Points

Each module:
1. Accepts target domain/IP
2. Runs the reconnaissance tool
3. Captures output
4. Parses results
5. Returns structured data
6. Contributes to final report

## Error Handling

- Command execution errors
- Tool not found errors
- Timeout handling
- Network error handling
- Permission denied handling

## Security Considerations

- Validates target input
- Handles sensitive data in output
- Creates output directories safely
- Respects tool timeout limits
- Logs all operations

## Future Enhancements

- Multi-target scanning
- Scheduled scanning
- Result comparison/tracking
- Advanced filtering
- Custom report templates
- API integration
- Database storage
- Web dashboard
- Slack notifications
- Proxy support
