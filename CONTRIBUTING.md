# Contributing to Reconnaissance Framework

Thank you for your interest in contributing to the Reconnaissance Framework! We welcome contributions from the community. This document provides guidelines for contributing.

## Code of Conduct

- Be respectful and inclusive
- Focus on constructive feedback
- Help others learn and grow
- Report security vulnerabilities responsibly

## How to Contribute

### Reporting Bugs

Before submitting a bug report, please check the issue list to avoid duplicates.

**To report a bug:**

1. **Use a clear, descriptive title**
2. **Describe the exact steps to reproduce**
3. **Provide specific examples to demonstrate**
4. **Describe the behavior you observed**
5. **Explain what you expected to see**
6. **Include screenshots if possible**

**Example bug report:**

```
Title: DNS enumeration fails with IPv6 addresses

Steps to reproduce:
1. Run: python3 main.py ::1 --mode dns
2. Command fails with error

Expected behavior:
Should handle IPv6 addresses gracefully

System:
- OS: Kali Linux 2024
- Python: 3.9
- Error message: [paste exact error]
```

### Suggesting Enhancements

**To suggest an enhancement:**

1. **Use a clear, descriptive title**
2. **Provide a step-by-step description**
3. **Provide specific examples**
4. **Explain why this would be useful**
5. **Consider performance implications**

**Example enhancement request:**

```
Title: Add Shodan integration for IP enumeration

Description:
Shodan could provide additional information about discovered IPs.

Implementation:
1. Create modules/shodan_scanner.py
2. Add Shodan API integration
3. Parse and format results

Benefits:
- More comprehensive reconnaissance
- Additional data sources
- Better insights into targets
```

### Pull Requests

**Before starting work:**

1. Check existing issues and PRs
2. Discuss major changes in an issue first
3. Fork the repository
4. Create a feature branch

**Development workflow:**

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/recon-framework.git
cd recon-framework

# Create feature branch
git checkout -b feature/amazing-feature

# Make changes
# Test thoroughly
# Commit with clear messages
git commit -m "Add amazing feature

- Describe what you did
- Explain why it's needed
- Note any breaking changes"

# Push to your fork
git push origin feature/amazing-feature

# Open a Pull Request on GitHub
```

**Commit message guidelines:**

- Use present tense ("Add feature" not "Added feature")
- Use imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit first line to 72 characters
- Reference issues and PRs liberally

### Code Style

**Python Code Standards:**

```python
# Follow PEP 8
# Use type hints where possible
def run_scan(target: str, timeout: int = 300) -> dict:
    """
    Run reconnaissance scan on target.
    
    Args:
        target: Domain name or IP address
        timeout: Timeout in seconds
    
    Returns:
        Dictionary containing scan results
    """
    pass

# Use descriptive names
correct_name = "scan_target"
wrong_name = "st"

# Comment complex logic
if isinstance(output, bytes):
    # Decode bytes to UTF-8 string
    output = output.decode('utf-8')

# Use logging instead of print
import logging
logger = logging.getLogger(__name__)
logger.info("Starting scan on %s", target)
```

**Module Structure:**

```python
#!/usr/bin/env python3
"""Module docstring explaining purpose and usage."""

import subprocess
import logging
from typing import Dict, List

logger = logging.getLogger(__name__)


class ScannerModule:
    """Class for handling specific reconnaissance tool."""
    
    def __init__(self, target: str):
        """Initialize with target."""
        self.target = target
        self.results = {}
    
    def _run_command(self, cmd: str) -> tuple:
        """Run command and return output."""
        try:
            result = subprocess.run(cmd, shell=True, ...)
            return result.stdout, result.stderr
        except Exception as e:
            logger.error("Command failed: %s", str(e))
            return "", str(e)
```

### Testing

**Writing Tests:**

```python
import unittest
from modules.dns_tools import DnsTools


class TestDnsTools(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures."""
        self.dns = DnsTools("example.com")
    
    def test_run_dig(self):
        """Test dig command execution."""
        result = self.dns.run_dig()
        self.assertIsNotNone(result)
        self.assertIn("output", result)
    
    def test_invalid_target(self):
        """Test handling of invalid targets."""
        dns = DnsTools("")
        result = dns.run_dig()
        self.assertIsNotNone(result.get("error"))


if __name__ == '__main__':
    unittest.main()
```

**Run tests:**

```bash
python3 -m unittest discover -s . -p "test_*.py"
```

### Documentation

**Update documentation for:**

- New features
- New modules
- API changes
- Bug fixes (if user-facing)

**Documentation format:**

- Use Markdown
- Include code examples
- Add warnings for breaking changes
- Update table of contents

### Areas for Contribution

#### 🐛 Bug Fixes
- Fix reported issues
- Improve error handling
- Handle edge cases

#### ✨ New Features
- Additional reconnaissance tools
- New scanning modes
- Enhanced reporting
- Performance improvements

#### 📚 Documentation
- Clarify existing docs
- Add examples
- Write tutorials
- Improve README

#### 🧪 Testing
- Write unit tests
- Add integration tests
- Improve test coverage
- Test on different systems

#### 💡 Performance
- Optimize slow operations
- Reduce memory usage
- Improve scan speed
- Better error handling

### Contributor Recognition

We recognize all contributions! Contributors will be listed in:
- `CONTRIBUTORS.md` file
- GitHub contributors page
- Release notes

## Development Setup

### Prerequisites

```bash
# Install Python 3.7+
python3 --version

# Install Git
git --version
```

### Setup Virtual Environment

```bash
# Create virtual environment
python3 -m venv venv

# Activate environment
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate  # Windows

# Install dependencies
pip3 install -r requirements.txt

# Install development tools
pip3 install pylint black pytest pytest-cov
```

### Code Quality

```bash
# Format code
black *.py modules/*.py

# Check style
pylint *.py modules/*.py

# Run tests
pytest -v

# Coverage report
pytest --cov=. --cov-report=html
```

## Release Process

When making a release:

1. Update version numbers
2. Update CHANGELOG
3. Update documentation
4. Create release notes
5. Tag commit with version
6. Create GitHub release

## Getting Help

- 📖 Read the [README.md](README.md)
- 📋 Check [FRAMEWORK_STRUCTURE.md](FRAMEWORK_STRUCTURE.md)
- 💬 Open a discussion
- 📧 Email maintainers

## Legal

By contributing to this project, you agree that:

- Your contributions can be used under the MIT License
- You have the right to contribute the code
- Your contribution does not violate any laws
- You understand security tool responsibilities

## Additional Notes

### Security Considerations

Since this is a security tool:

- Never hardcode credentials
- Validate all user inputs
- Handle errors securely
- Don't log sensitive data
- Follow security best practices

### Performance

For reconnaissance tools:

- Consider timeout values
- Avoid blocking operations
- Minimize resource usage
- Cache results when possible
- Support concurrent operations

### Compatibility

Maintain compatibility with:

- Python 3.7+
- Kali Linux 2023+
- Standard Linux distros
- Docker environments

## Questions?

- Open an issue
- Start a discussion
- Contact maintainers
- Check documentation

---

**Thank you for contributing! 🎉**
