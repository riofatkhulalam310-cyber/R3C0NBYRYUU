#!/usr/bin/env python3
"""
Amass Scanner Module
"""

import subprocess
import json
import re


class AmassScanner:
    def __init__(self, target):
        self.target = target
        self.results = {}
    
    def _run_command(self, cmd):
        """Run command and return output"""
        try:
            result = subprocess.run(
                cmd,
                shell=True,
                capture_output=True,
                text=True,
                timeout=180
            )
            return result.stdout, result.stderr
        except subprocess.TimeoutExpired:
            return "", "Command timed out"
        except Exception as e:
            return "", str(e)
    
    def enumerate(self):
        """Run Amass enumeration"""
        cmd = f"amass enum -d {self.target}"
        stdout, stderr = self._run_command(cmd)
        
        self.results["amass_enum"] = {
            "command": cmd,
            "output": stdout,
            "error": stderr if stderr else None
        }
        return self.results["amass_enum"]
    
    def enumerate_verbose(self):
        """Run Amass enumeration with verbose output"""
        cmd = f"amass enum -d {self.target} -v"
        stdout, stderr = self._run_command(cmd)
        
        self.results["amass_verbose"] = {
            "command": cmd,
            "output": stdout,
            "error": stderr if stderr else None
        }
        return self.results["amass_verbose"]
    
    def intel_gather(self):
        """Run Amass intel gathering"""
        cmd = f"amass intel -d {self.target}"
        stdout, stderr = self._run_command(cmd)
        
        self.results["amass_intel"] = {
            "command": cmd,
            "output": stdout,
            "error": stderr if stderr else None
        }
        return self.results["amass_intel"]
    
    def track_domains(self):
        """Track domains using Amass"""
        cmd = f"amass track -d {self.target}"
        stdout, stderr = self._run_command(cmd)
        
        self.results["amass_track"] = {
            "command": cmd,
            "output": stdout,
            "error": stderr if stderr else None
        }
        return self.results["amass_track"]
    
    def parse_results(self):
        """Parse Amass results"""
        parsed = {
            "subdomains": [],
            "ips": []
        }
        
        for result in self.results.values():
            output = result.get("output", "")
            
            # Extract subdomains (lines that end with the target domain)
            lines = output.split('\n')
            for line in lines:
                line = line.strip()
                # Look for DNS entries (typically shown as subdomain -> IP)
                if ' -> ' in line:
                    parts = line.split(' -> ')
                    if len(parts) == 2:
                        subdomain = parts[0].strip()
                        ip = parts[1].strip()
                        if self.target in subdomain:
                            parsed["subdomains"].append(subdomain)
                        parsed["ips"].append(ip)
                elif self.target in line and not line.startswith('['):
                    # Look for direct subdomain mentions
                    subdomains = re.findall(r'(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+' + re.escape(self.target), line)
                    parsed["subdomains"].extend(subdomains)
            
            # Extract IPs
            ips = re.findall(r'\d+\.\d+\.\d+\.\d+', output)
            parsed["ips"].extend(ips)
        
        # Remove duplicates
        parsed["subdomains"] = list(set(parsed["subdomains"]))
        parsed["ips"] = list(set(parsed["ips"]))
        
        return parsed
