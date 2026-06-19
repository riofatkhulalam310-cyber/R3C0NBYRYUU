# Repository Contents & Documentation Index

Complete guide to all files and documentation in the Reconnaissance Framework repository.

## 📁 Directory Structure

```
recon-framework/
│
├── 📚 DOCUMENTATION FILES
│   ├── README.md                    # Main project documentation (START HERE!)
│   ├── INSTALLATION.md              # Step-by-step installation guide
│   ├── QUICK_REFERENCE.md           # Command reference card
│   ├── FAQ.md                       # Frequently asked questions
│   ├── BEST_PRACTICES.md            # Usage best practices
│   ├── FRAMEWORK_STRUCTURE.md       # Technical architecture details
│   ├── CHANGELOG.md                 # Version history and changes
│   ├── CONTRIBUTING.md              # Contribution guidelines
│   ├── SECURITY.md                  # Security policies
│   ├── LICENSE                      # MIT License
│   └── INDEX.md                     # This file
│
├── 🐍 PYTHON CORE FILES
│   ├── main.py                      # Main framework entry point
│   ├── report_generator.py          # HTML report generation
│   ├── examples.py                  # Interactive examples menu
│   ├── requirements.txt             # Python dependencies
│   │
│   └── modules/                     # Reconnaissance tool modules
│       ├── __init__.py              # Module initialization
│       ├── nmap_scanner.py          # Nmap port scanner wrapper
│       ├── dns_tools.py             # DNS enumeration (dig/nslookup)
│       ├── harvester.py             # TheHarvester wrapper
│       ├── amass_scanner.py         # Amass subdomain enumeration
│       └── gobuster_scanner.py      # Gobuster directory enumeration
│
├── ⚙️ CONFIGURATION FILES
│   └── config/
│       └── config.ini               # Framework configuration
│
├── 🐳 DOCKER FILES
│   ├── Dockerfile                   # Docker image definition
│   ├── docker-build.sh              # Build Docker image
│   └── docker-run.sh                # Run in Docker container
│
├── 📜 SHELL SCRIPTS
│   ├── install.sh                   # Automated installation script
│   ├── run.sh                       # Quick run wrapper
│   └── setup-permissions.sh         # Set executable permissions
│
├── 📂 DIRECTORIES (Auto-created)
│   └── output/                      # Reconnaissance results
│
├── 🔧 GIT FILES
│   ├── .gitignore                   # Git ignore patterns
│   └── .github/
│       └── workflows/
│           └── tests.yml            # CI/CD test workflow
│
└── 📊 THIS FILE
    └── INDEX.md                     # Documentation index
```

---

## 📖 Documentation Guide

### For Getting Started

1. **[README.md](README.md)** ⭐ **START HERE**
   - Project overview
   - Feature list
   - Quick start examples
   - Basic usage

2. **[INSTALLATION.md](INSTALLATION.md)**
   - Prerequisites
   - Step-by-step installation
   - Verification checklist
   - Troubleshooting

3. **[QUICK_REFERENCE.md](QUICK_REFERENCE.md)**
   - Common commands
   - Quick reference
   - Examples

### For Understanding the Framework

4. **[FRAMEWORK_STRUCTURE.md](FRAMEWORK_STRUCTURE.md)**
   - System architecture
   - Module descriptions
   - Data flow
   - Integration points

5. **[BEST_PRACTICES.md](BEST_PRACTICES.md)**
   - Legal/authorization
   - Planning
   - Scanning best practices
   - Performance optimization
   - Security practices

### For Using the Framework

6. **[FAQ.md](FAQ.md)**
   - Installation Q&A
   - Usage questions
   - Troubleshooting
   - Advanced topics

### For Contributing

7. **[CONTRIBUTING.md](CONTRIBUTING.md)**
   - How to contribute
   - Code style
   - Testing guidelines
   - Pull request process

### For Security & Legal

8. **[SECURITY.md](SECURITY.md)**
   - Security policies
   - Vulnerability reporting
   - Legal compliance
   - Best practices

### For Tracking Changes

9. **[CHANGELOG.md](CHANGELOG.md)**
   - Version history
   - Feature additions
   - Bug fixes
   - Roadmap

---

## 🐍 Python Files

### Core Application

| File | Purpose | Type |
|------|---------|------|
| `main.py` | Framework controller | Entry point |
| `report_generator.py` | HTML report creation | Utility |
| `examples.py` | Interactive examples | Menu |

### Reconnaissance Modules

| File | Purpose | Tool |
|------|---------|------|
| `modules/nmap_scanner.py` | Port scanning | Nmap |
| `modules/dns_tools.py` | DNS enumeration | dig/nslookup |
| `modules/harvester.py` | Email discovery | TheHarvester |
| `modules/amass_scanner.py` | Subdomain enumeration | Amass |
| `modules/gobuster_scanner.py` | Directory brute force | Gobuster |

### Configuration & Dependencies

| File | Purpose |
|------|---------|
| `config/config.ini` | Framework settings |
| `requirements.txt` | Python packages |

---

## 🔧 Configuration & Deployment

### Configuration

- **`config/config.ini`**
  - Tool enable/disable settings
  - Timeout configuration
  - Wordlist paths
  - Output settings
  - Default parameters

### Docker

- **`Dockerfile`** - Container image definition
- **`docker-build.sh`** - Build automation
- **`docker-run.sh`** - Execution wrapper

### Installation

- **`install.sh`** - Automated installer
- **`run.sh`** - Quick run script
- **`setup-permissions.sh`** - Permission setup

---

## 📋 File Reading Guide

### 5-Minute Overview

Read in order:
1. This file (INDEX.md)
2. README.md - Features & overview
3. QUICK_REFERENCE.md - Commands

**Total time**: 5 minutes

### 30-Minute Quick Start

Read in order:
1. README.md - Full overview
2. INSTALLATION.md - Setup steps
3. QUICK_REFERENCE.md - Commands

**Total time**: 30 minutes

### Complete Understanding (1 Hour)

Read in order:
1. README.md - Overview
2. INSTALLATION.md - Setup
3. FRAMEWORK_STRUCTURE.md - Architecture
4. FAQ.md - Q&A
5. BEST_PRACTICES.md - Best practices

**Total time**: 1 hour

### Full Master (2-3 Hours)

Read all documentation files:
1. README.md
2. INSTALLATION.md
3. FRAMEWORK_STRUCTURE.md
4. FAQ.md
5. BEST_PRACTICES.md
6. CONTRIBUTING.md
7. SECURITY.md
8. CHANGELOG.md

**Total time**: 2-3 hours

---

## 📂 Output & Results

### Output Directory Structure

```
output/
├── recon_target1.com_20240101_120000.json
├── recon_target1.com_20240101_120000.html
├── recon_target2.com_20240101_150000.json
├── recon_target2.com_20240101_150000.html
└── ...
```

### File Naming Convention

```
recon_<TARGET>_<YYYYMMDD>_<HHMMSS>.json
recon_<TARGET>_<YYYYMMDD>_<HHMMSS>.html

Example:
recon_example.com_20240101_120000.json
recon_192.168.1.1_20240101_120000.json
```

---

## 🚀 Quick Start Paths

### Path 1: Just Get It Working
```
1. Read: README.md (Features section)
2. Read: INSTALLATION.md (Automated Installation)
3. Run: sudo ./install.sh
4. Run: python3 main.py example.com --mode full
5. Check: output/ for results
```

### Path 2: Understand Everything First
```
1. Read: README.md (Complete)
2. Read: FRAMEWORK_STRUCTURE.md
3. Read: INSTALLATION.md
4. Read: BEST_PRACTICES.md
5. Run: python3 main.py example.com --mode dns
6. Gradually try other modes
```

### Path 3: Already Experienced
```
1. Skim: README.md (Feature list)
2. Check: QUICK_REFERENCE.md
3. Review: FRAMEWORK_STRUCTURE.md (Architecture)
4. Start: python3 main.py <target> --mode full
5. Reference: FAQ.md if issues
```

### Path 4: Want to Contribute
```
1. Read: CONTRIBUTING.md
2. Read: FRAMEWORK_STRUCTURE.md
3. Review: modules/ code
4. Check: open issues on GitHub
5. Create: pull request with improvements
```

---

## 📚 Documentation by Topic

### Installation & Setup
- [INSTALLATION.md](INSTALLATION.md) - Complete installation guide
- [README.md](README.md) - Quick start section
- [FAQ.md](FAQ.md) - Installation Q&A

### Usage & Commands
- [README.md](README.md) - Usage section
- [QUICK_REFERENCE.md](QUICK_REFERENCE.md) - Command reference
- [FAQ.md](FAQ.md) - Usage questions

### Architecture & Design
- [FRAMEWORK_STRUCTURE.md](FRAMEWORK_STRUCTURE.md) - Technical details
- [README.md](README.md) - Architecture section

### Best Practices & Security
- [BEST_PRACTICES.md](BEST_PRACTICES.md) - Comprehensive guide
- [SECURITY.md](SECURITY.md) - Security policies
- [README.md](README.md) - Tips section

### Tools & Modules
- [README.md](README.md) - Tools overview
- [FRAMEWORK_STRUCTURE.md](FRAMEWORK_STRUCTURE.md) - Module descriptions

### Troubleshooting
- [FAQ.md](FAQ.md) - Troubleshooting section
- [INSTALLATION.md](INSTALLATION.md) - Installation issues
- [README.md](README.md) - Common issues

### Contributing & Development
- [CONTRIBUTING.md](CONTRIBUTING.md) - Full guide
- [CHANGELOG.md](CHANGELOG.md) - Version history

---

## 🔍 Finding Information

### By Question

**Q: How do I install?**
→ [INSTALLATION.md](INSTALLATION.md)

**Q: How do I use this?**
→ [README.md](README.md) + [QUICK_REFERENCE.md](QUICK_REFERENCE.md)

**Q: How does it work?**
→ [FRAMEWORK_STRUCTURE.md](FRAMEWORK_STRUCTURE.md)

**Q: What are best practices?**
→ [BEST_PRACTICES.md](BEST_PRACTICES.md)

**Q: I have a problem**
→ [FAQ.md](FAQ.md) + [INSTALLATION.md](INSTALLATION.md)

**Q: Is it legal?**
→ [SECURITY.md](SECURITY.md) + [BEST_PRACTICES.md](BEST_PRACTICES.md)

**Q: How do I contribute?**
→ [CONTRIBUTING.md](CONTRIBUTING.md)

**Q: What changed?**
→ [CHANGELOG.md](CHANGELOG.md)

---

## 📞 Support & Resources

### Getting Help
1. Check [FAQ.md](FAQ.md) for common questions
2. Search [README.md](README.md) for features
3. Review [BEST_PRACTICES.md](BEST_PRACTICES.md) for guidance
4. Open GitHub issue for problems
5. Check [CONTRIBUTING.md](CONTRIBUTING.md) for support options

### Documentation Links
- 📖 [Main README](README.md)
- 🔧 [Installation Guide](INSTALLATION.md)
- 📋 [Framework Structure](FRAMEWORK_STRUCTURE.md)
- ❓ [FAQ](FAQ.md)
- 🎯 [Best Practices](BEST_PRACTICES.md)
- 🤝 [Contributing](CONTRIBUTING.md)
- 🔒 [Security](SECURITY.md)
- 📅 [Changelog](CHANGELOG.md)

---

## ✅ Documentation Checklist

Before using the framework, review:

```
For New Users:
☐ README.md - Overview and features
☐ INSTALLATION.md - Installation steps
☐ QUICK_REFERENCE.md - Common commands
☐ FAQ.md - Common questions

For Experienced Users:
☐ FRAMEWORK_STRUCTURE.md - Architecture
☐ BEST_PRACTICES.md - Best practices
☐ config/config.ini - Configuration

For Contributors:
☐ CONTRIBUTING.md - Guidelines
☐ FRAMEWORK_STRUCTURE.md - Code structure
☐ SECURITY.md - Security practices
```

---

## 📊 Files at a Glance

| File | Size | Audience | Time |
|------|------|----------|------|
| README.md | Large | Everyone | 15 min |
| INSTALLATION.md | Large | New users | 20 min |
| QUICK_REFERENCE.md | Small | All users | 5 min |
| FRAMEWORK_STRUCTURE.md | Large | Developers | 20 min |
| FAQ.md | Very Large | Problem solvers | 30 min |
| BEST_PRACTICES.md | Very Large | Professionals | 30 min |
| CONTRIBUTING.md | Large | Contributors | 15 min |
| SECURITY.md | Large | Security teams | 20 min |
| CHANGELOG.md | Medium | Version tracking | 10 min |

---

## 🎓 Learning Path Recommendations

### Beginner
```
1. README.md (Features & Quick Start)      → 10 min
2. INSTALLATION.md (Automated setup)        → 5 min
3. QUICK_REFERENCE.md (Commands)           → 5 min
Total: 20 minutes
```

### Intermediate
```
1. README.md (Complete)                     → 15 min
2. INSTALLATION.md (Complete)               → 15 min
3. FAQ.md (First half)                      → 10 min
4. BEST_PRACTICES.md (Scanning section)    → 10 min
Total: 50 minutes
```

### Advanced
```
1. FRAMEWORK_STRUCTURE.md (Complete)       → 20 min
2. BEST_PRACTICES.md (Complete)            → 30 min
3. SECURITY.md (Complete)                  → 20 min
4. CONTRIBUTING.md (Complete)              → 15 min
Total: 85 minutes
```

---

## 🔗 Cross-References

### Documentation Links
- See [README.md](README.md#features) for feature list
- See [INSTALLATION.md](INSTALLATION.md#system-requirements) for requirements
- See [FRAMEWORK_STRUCTURE.md](FRAMEWORK_STRUCTURE.md#project-structure) for structure
- See [FAQ.md](FAQ.md#installation--setup) for FAQ
- See [BEST_PRACTICES.md](BEST_PRACTICES.md#-legal--authorization) for legal info

### External Resources
- [GitHub Repository](https://github.com/yourusername/recon-framework)
- [Issue Tracker](https://github.com/yourusername/recon-framework/issues)
- [Discussions](https://github.com/yourusername/recon-framework/discussions)
- [Security Policy](SECURITY.md)

---

## 📝 Document Versions

| Document | Purpose | Last Updated |
|----------|---------|--------------|
| README.md | Main documentation | 2024-01-01 |
| INSTALLATION.md | Setup guide | 2024-01-01 |
| QUICK_REFERENCE.md | Command reference | 2024-01-01 |
| FRAMEWORK_STRUCTURE.md | Architecture | 2024-01-01 |
| FAQ.md | Q&A | 2024-01-01 |
| BEST_PRACTICES.md | Practices guide | 2024-01-01 |
| CONTRIBUTING.md | Contribution guide | 2024-01-01 |
| SECURITY.md | Security policy | 2024-01-01 |
| CHANGELOG.md | Version history | 2024-01-01 |
| INDEX.md | This file | 2024-01-01 |

---

## 🎯 Next Steps

1. **Choose Your Path**
   - New to the framework? → Start with README.md
   - Need to install? → Go to INSTALLATION.md
   - Have questions? → Check FAQ.md
   - Want to contribute? → Read CONTRIBUTING.md

2. **Start Using It**
   - Install following INSTALLATION.md
   - Run first scan: `python3 main.py example.com`
   - Check output in `output/` directory

3. **Get Proficient**
   - Review QUICK_REFERENCE.md
   - Read BEST_PRACTICES.md
   - Try different scan modes

4. **Advance Your Skills**
   - Study FRAMEWORK_STRUCTURE.md
   - Review module code
   - Contribute improvements

---

**Welcome to Reconnaissance Framework! 🚀**

Start with [README.md](README.md) or [INSTALLATION.md](INSTALLATION.md) depending on your needs.

---

**Last Updated**: 2024-01-01
**Framework Version**: 1.0.0
**Status**: ✅ Complete & Ready for Use
