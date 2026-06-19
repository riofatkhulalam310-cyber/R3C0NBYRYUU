# Best Practices Guide

Complete guide for using the Reconnaissance Framework effectively and responsibly.

## Table of Contents

- [Legal & Authorization](#-legal--authorization)
- [Planning Your Reconnaissance](#-planning-your-reconnaissance)
- [Scanning Best Practices](#-scanning-best-practices)
- [Performance Optimization](#-performance-optimization)
- [Results Analysis](#-results-analysis)
- [Reporting](#-reporting)
- [Security Practices](#-security-practices)

---

## 🔒 Legal & Authorization

### Get Written Authorization

**Before any reconnaissance:**

1. **Scope Document**
   ```
   Company Name: [Client]
   Authorized Targets: [Specific domains/IPs]
   Testing Period: [Start date] - [End date] [Time window]
   Testing Types: Network reconnaissance, port scanning
   Authorized Tester: [Your name/company]
   Contact: [Your contact info]
   ```

2. **Signed Agreement**
   - Get written authorization from system owner
   - Define scope clearly
   - Specify restricted areas
   - Liability terms
   - Confidentiality

3. **Rules of Engagement**
   - Do NOT: [specific restrictions]
   - Avoid: [critical systems, peak hours]
   - Notify: [contact for issues]
   - Stop: [stop criteria/conditions]

### Maintain Documentation

```bash
# Create project documentation
mkdir project_docs
cp authorization.pdf project_docs/
echo "Target: example.com" > project_docs/scope.txt
echo "Date: 2024-01-01" >> project_docs/scope.txt

# Keep version control
git init project_docs
git add .
git commit -m "Initial authorization and scope"
```

---

## 📋 Planning Your Reconnaissance

### 1. Define Objectives

**Question to answer:**
- ✅ What are we trying to find out?
- ✅ What's the scope?
- ✅ What systems are in scope?
- ✅ What's the timeline?
- ✅ What are the success criteria?

### 2. Create Reconnaissance Plan

```markdown
# Reconnaissance Plan - Example.com

## Objectives
- Identify all public IP addresses
- Discover subdomains
- Enumerate open ports
- Identify services
- Find email addresses

## Scope
- Authorized: example.com, *.example.com
- Excluded: internal.example.com, admin.example.com
- Testing period: 2024-01-01 to 2024-01-07

## Methodology
- Phase 1: Passive reconnaissance (DNS, WHOIS)
- Phase 2: Active reconnaissance (port scan, service enumeration)
- Phase 3: Application enumeration
- Phase 4: Analysis and reporting

## Timeline
- Day 1: Planning and authorization
- Day 2-3: Passive reconnaissance
- Day 4-5: Active reconnaissance
- Day 6: Analysis
- Day 7: Reporting

## Success Criteria
- All subdomains identified
- All open ports found
- Services identified
- Report completed and approved
```

### 3. Set Realistic Expectations

```bash
# Estimate time needed
- DNS enumeration: 5-10 minutes
- Basic Nmap: 30-60 seconds
- Aggressive Nmap: 5-15 minutes
- Harvester: 3-10 minutes
- Amass: 5-30 minutes
- Gobuster: 10-60 minutes (depends on wordlist)

# Total: 30-120 minutes for full scan
```

### 4. Create Inventory

```bash
# Create target list
cat > targets.txt << EOF
example.com
mail.example.com
web.example.com
EOF

# Or use input file
python3 main.py -i targets.txt --mode full
```

---

## 🎯 Scanning Best Practices

### 1. Start Small, Then Grow

```bash
# Phase 1: Test with single tool
python3 main.py example.com --mode dns

# Phase 2: Add port scanning
python3 main.py example.com --mode nmap --nmap-type basic

# Phase 3: Full reconnaissance
python3 main.py example.com --mode full
```

### 2. Choose Appropriate Scan Types

| Situation | Recommendation |
|-----------|----------------|
| Production system | Basic DNS + minimal Nmap |
| Development system | Full scan OK |
| Off-hours | Aggressive scan acceptable |
| Client request | Ask what they prefer |
| Permission unclear | Conservative approach |
| First time on target | Start very minimal |

### 3. Monitor Impact

```bash
# Before scanning
ping -c 1 example.com

# Monitor during scan
watch -n 5 'netstat -an | grep ESTABLISHED | wc -l'

# Check target status
curl -I https://example.com

# After scanning
ping -c 1 example.com
```

### 4. Use Appropriate Timing

```bash
# Check if target is production
# Scan during:
- Night hours
- Weekends
- Maintenance windows
- Low-traffic periods

# Avoid scanning during:
- Business hours
- Known high-traffic times
- Critical operations
- Deployment windows
```

### 5. Set Resource Limits

```bash
# Limit Gobuster threads
python3 main.py example.com --mode gobuster \
    --wordlist /small/list.txt

# Configure config.ini
[General]
timeout = 300  # 5 minutes max per tool

[Gobuster]
threads = 10  # Reduced from 50
```

---

## ⚡ Performance Optimization

### 1. Use Appropriate Wordlists

| Target Type | Wordlist | Size | Time |
|-------------|----------|------|------|
| Small site | small.txt | <100 | <1min |
| Medium site | medium.txt | 1000 | 5-10min |
| Large site | large.txt | 10000 | 30-60min |
| Full assessment | big.txt | 100000+ | 2-4hrs |

```bash
# Use smaller wordlist for speed
python3 main.py example.com --mode gobuster \
    --wordlist /usr/share/wordlists/dirb/small.txt

# For thorough scan
python3 main.py example.com --mode gobuster \
    --wordlist /usr/share/wordlists/dirb/big.txt
```

### 2. Selective Scanning

```bash
# Skip slow modules
python3 main.py example.com --mode dns
python3 main.py example.com --mode nmap

# Instead of full scan that includes slow modules
```

### 3. Parallel Execution

```bash
# Run multiple targets simultaneously
python3 main.py target1.com --mode full &
python3 main.py target2.com --mode full &
python3 main.py target3.com --mode full &

# Wait for completion
wait

# Check results
ls output/recon_*.json
```

### 4. Caching Results

```bash
# Save results for later analysis
jq '.' output/recon_example.com_*.json > results.json

# Reuse for different analysis without re-scanning
cat results.json | jq '.results.dns'
```

### 5. Distributed Scanning

```bash
# Split targets across multiple systems
# System 1
for target in target1.com target2.com; do
    python3 main.py $target --mode dns
done

# System 2
for target in target3.com target4.com; do
    python3 main.py $target --mode harvester
done
```

---

## 🔍 Results Analysis

### 1. Organize Results

```bash
# Create analysis directory
mkdir analysis
cd analysis

# Copy and extract results
cp ../output/recon_*.json .

# Organize by target
for file in recon_*.json; do
    target=$(echo $file | sed 's/recon_//;s/_[0-9]*.json//')
    mkdir -p $target
    mv $file $target/
done
```

### 2. Extract Key Information

```bash
# Extract all IPs found
jq '.results | .. | .ips? | select(. != null) | .[]' output/recon_*.json

# Extract all subdomains
jq '.results | .. | .subdomains? | select(. != null) | .[]' output/recon_*.json

# Extract open ports
jq '.results.nmap | .. | .port? | select(. != null)' output/recon_*.json

# Extract emails
jq '.results.harvester | .. | select(test("@")) | @text' output/recon_*.json
```

### 3. Create Summary

```bash
# Consolidate findings
cat > findings_summary.md << EOF
# Reconnaissance Findings - Example.com

## Discovered Subdomains
EOF

# Add subdomains
jq -r '.results.amass.subdomains[]' output/recon_*.json | sort -u >> findings_summary.md

echo "
## Open Ports
" >> findings_summary.md

# Add open ports
jq -r '.results.nmap.basic_scan.output' output/recon_*.json | grep "open" >> findings_summary.md
```

### 4. Cross-Reference Data

```
DNS Records:
- IPs: 1.2.3.4, 5.6.7.8
- Nameservers: ns1.example.com, ns2.example.com

Nmap Results:
- Port 80 open (HTTP)
- Port 443 open (HTTPS)

TheHarvester:
- 15 emails found
- 12 subdomains

Amass:
- 28 subdomains found

Conclusion:
- 3 main IP addresses
- 25+ subdomains
- Web services running
```

### 5. Identify Quick Wins

```bash
# Find potentially vulnerable services
jq '.results.nmap | .. | select(.service == "Apache") | .' output/recon_*.json

# Find outdated services
jq '.results.nmap | .. | select(.version | test("1\\.")) | .' output/recon_*.json
```

---

## 📊 Reporting

### 1. Create Report Structure

```bash
mkdir -p report
mkdir -p report/screenshots
mkdir -p report/data

# Copy raw data
cp output/recon_*.json report/data/

# Generate HTML
python3 report_generator.py output/recon_*.json > report/report.html
```

### 2. Report Components

```markdown
# Reconnaissance Report - Example.com

## Executive Summary
- Scope and objectives
- High-level findings
- Risk assessment

## Methodology
- Tools used
- Scan types
- Timeline

## Findings
- Discovered subdomains
- Open ports and services
- Email addresses
- Infrastructure details

## Recommendations
- Quick wins
- Security improvements
- Further testing

## Appendix
- Raw data
- Tool outputs
- Detailed analysis
```

### 3. Include Evidence

```bash
# Screenshot of results
cat output/recon_example.com_*.json | jq '.' > report/raw_data.json

# HTML report
python3 report_generator.py output/recon_*.json > report/formatted_report.html

# Summary table
jq '.results | keys' output/recon_*.json > report/scan_modules_used.txt
```

### 4. Protect Sensitive Data

```bash
# Redact or remove sensitive information
sed -i 's/internal-api/[REDACTED]/g' report/report.html

# Set file permissions
chmod 600 report/*

# Encrypt if needed
gpg -c report/report.html
```

### 5. Get Approval

```
☐ Results verified
☐ Sensitive data removed
☐ Recommendations realistic
☐ Timeline accurate
☐ Client reviewed
☐ Final approval obtained
```

---

## 🔒 Security Practices

### 1. Protect Your Infrastructure

```bash
# Use VPN or proxy
export HTTP_PROXY=socks5://10.0.0.1:1080

# Run from isolated network
# Use jump box or bastion host

# Monitor your own system
netstat -an | wc -l

# Check logs
journalctl -n 100
```

### 2. Secure Your Data

```bash
# Encrypt results
gpg --symmetric output/recon_*.json

# Use secure storage
tar -czf results.tar.gz output/
gpg --encrypt results.tar.gz
rm -shred results.tar.gz

# Secure deletion
shred -vfz -n 3 output/recon_*.json
```

### 3. Log Everything

```bash
# Create audit log
cat > audit.log << EOF
Date: 2024-01-01
Target: example.com
Tester: John Doe
Authorization: See auth.pdf
Scope: example.com, *.example.com
Exclusions: internal.example.com
Time Started: 14:00
Time Completed: 14:45
Tools Used: DNS, Nmap, Harvester, Amass, Gobuster
Findings: 25 subdomains, 5 open ports
Issues: None
Sign-off: ___________
EOF
```

### 4. Incident Response

```bash
# If issues occur:

# 1. Stop immediately
Ctrl+C

# 2. Document
echo "Scan halted - service degradation detected" >> audit.log
echo "Time: $(date)" >> audit.log

# 3. Investigate
ping target
curl -I https://target

# 4. Report
Contact: client_contact@example.com
Message: "Reconnaissance paused due to service issues"

# 5. Resume carefully
# Only continue with explicit approval
```

### 5. Post-Scan Cleanup

```bash
# Remove tools and data if needed
# But keep audit trail

# Archive results
tar -czf archive_2024_01.tar.gz output/
gpg --encrypt archive_2024_01.tar.gz

# Clean temporary files
rm -f temp_*

# Verify cleanup
ls -la | grep -E "output|temp"
```

---

## 📈 Metrics & Reporting

### Track Key Metrics

```bash
# Number of targets
wc -l targets.txt

# Scan duration
START=$(date +%s)
# ... run scans ...
END=$(date +%s)
echo "Duration: $((END-START)) seconds"

# Findings per target
jq '.target' output/recon_*.json | sort | uniq -c

# Average findings
jq '.results | keys | length' output/recon_*.json | \
    awk '{sum+=$1} END {print sum/NR}'
```

### Create Dashboard

```bash
# Simple metric output
cat > metrics.txt << EOF
Total Targets: 5
Total Scans: 5
Success Rate: 100%
Average Duration: 45 minutes
Average Findings: 25
Total Subdomains: 125
Total Open Ports: 15
Total Emails: 45
EOF
```

---

## 🎓 Continuous Improvement

### After Each Assessment

1. **Document Lessons Learned**
   - What worked well?
   - What could be improved?
   - New tools or techniques discovered?

2. **Update Procedures**
   - Refine scan profiles
   - Optimize tool parameters
   - Improve reporting

3. **Share Knowledge**
   - Contribute to team knowledge base
   - Share findings with colleagues
   - Update internal documentation

### Regular Training

```bash
# Stay current
- Follow security blogs
- Watch security conferences
- Participate in CTF challenges
- Read tool documentation

# Practice
- Set up lab environment
- Practice on test domains
- Experiment with new tools
- Refine techniques
```

---

## ✅ Pre-Scan Checklist

```
AUTHORIZATION & PLANNING
☐ Written authorization obtained
☐ Scope clearly defined
☐ Timeline established
☐ Objectives documented
☐ Stakeholders notified
☐ Emergency contacts listed

TECHNICAL PREPARATION
☐ Tools installed and tested
☐ Network connectivity verified
☐ VPN/Proxy configured if needed
☐ Disk space available
☐ System performance checked
☐ Backups created

SECURITY PREPARATION
☐ Firewall rules configured
☐ Encryption enabled
☐ Audit logging enabled
☐ Incident response plan ready
☐ Communication plan established
☐ Risk assessment completed

EXECUTION
☐ Start with minimal scans
☐ Monitor for issues
☐ Document progress
☐ Maintain logs
☐ Save results
☐ Verify data integrity
```

---

## 📞 When Something Goes Wrong

### Stop Immediately

```bash
# 1. Interrupt scan
Ctrl+C

# 2. Document time
echo "$(date): Scan stopped - service degradation" >> incident.log

# 3. Assess situation
curl -I https://target
ping target

# 4. Notify stakeholders
# Send alert to authorized contact

# 5. Wait for guidance
# Follow incident response procedures
```

### Recovery

```bash
# 1. Wait for clearance
# Contact: [authorized contact]

# 2. Verify target stability
# Check if service has recovered

# 3. Reduce scan intensity
# Use basic scans instead of aggressive

# 4. Resume with approval
# Get written confirmation before continuing
```

---

## 🎯 Success Criteria

✅ **Successful Assessment**
- All objectives achieved
- No unplanned downtime
- Results verified
- Report approved
- Lessons documented

⚠️ **Partial Success**
- Some objectives achieved
- Minor issues encountered
- Issues documented
- Alternative approach noted

❌ **Failed Assessment**
- Major issues occurred
- Service degradation
- Incident response activated
- Post-mortem completed

---

## 📚 Additional Resources

- [README.md](README.md) - Framework overview
- [FAQ.md](FAQ.md) - Common questions
- [SECURITY.md](SECURITY.md) - Security policies
- [CONTRIBUTING.md](CONTRIBUTING.md) - Contribution guidelines

---

**Remember**: The best reconnaissance is one that's authorized, planned, executed carefully, and properly documented.

---

**Last Updated**: 2024-01-01
