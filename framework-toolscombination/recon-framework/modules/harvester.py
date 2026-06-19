#!/usr/bin/env python3
"""
TheHarvester Module
"""

import subprocess
import json
import re


class HarvesterTools:
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
                timeout=120
            )
            return result.stdout, result.stderr
        except subprocess.TimeoutExpired:
            return "", "Command timed out"
        except Exception as e:
            return "", str(e)
    
    def search(self, limit=500):
        """Run TheHarvester search"""
        cmd = f"theHarvester -d {self.target} -l {limit} -b all"
        stdout, stderr = self._run_command(cmd)
        
        self.results["harvester_search"] = {
            "command": cmd,
            "output": stdout,
            "error": stderr if stderr else None
        }
        return self.results["harvester_search"]
    
    def search_by_source(self, source):
        """Search by specific source (google, bing, linkedin, etc)"""
        cmd = f"theHarvester -d {self.target} -b {source}"
        stdout, stderr = self._run_command(cmd)
        
        if source not in self.results:
            self.results[f"harvester_{source}"] = {}
        
        self.results[f"harvester_{source}"] = {
            "command": cmd,
            "output": stdout,
            "error": stderr if stderr else None
        }
        return self.results[f"harvester_{source}"]
    
    def search_emails(self):
        """Search for email addresses"""
        cmd = f"theHarvester -d {self.target} -b google,bing,linkedin"
        stdout, stderr = self._run_command(cmd)
        
        self.results["harvester_emails"] = {
            "command": cmd,
            "output": stdout,
            "error": stderr if stderr else None
        }
        return self.results["harvester_emails"]
    
    def parse_results(self):
        """Parse TheHarvester results"""
        parsed = {
            "emails": [],
            "subdomains": [],
            "ips": []
        }
        
        for result in self.results.values():
            output = result.get("output", "")
            
            # Extract emails
            emails = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', output)
            parsed["emails"].extend(emails)
            
            # Extract subdomains
            subdomains = re.findall(r'(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+' + re.escape(self.target), output)
            parsed["subdomains"].extend(subdomains)
            
            # Extract IPs
            ips = re.findall(r'\d+\.\d+\.\d+\.\d+', output)
            parsed["ips"].extend(ips)
        
        # Remove duplicates
        parsed["emails"] = list(set(parsed["emails"]))
        parsed["subdomains"] = list(set(parsed["subdomains"]))
        parsed["ips"] = list(set(parsed["ips"]))
        
        return parsed
