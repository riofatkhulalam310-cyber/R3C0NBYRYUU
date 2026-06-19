#!/usr/bin/env python3
"""
Gobuster Scanner Module
"""

import subprocess
import re


class GobusterScanner:
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
                timeout=600
            )
            return result.stdout, result.stderr
        except subprocess.TimeoutExpired:
            return "", "Command timed out"
        except Exception as e:
            return "", str(e)
    
    def enumerate_directories(self, wordlist="common.txt", extensions="php,html,txt"):
        """Enumerate directories"""
        cmd = f"gobuster dir -u http://{self.target} -w {wordlist} -x {extensions} -q"
        stdout, stderr = self._run_command(cmd)
        
        self.results["dir_enum"] = {
            "command": cmd,
            "output": stdout,
            "error": stderr if stderr else None
        }
        return self.results["dir_enum"]
    
    def enumerate_directories_https(self, wordlist="common.txt", extensions="php,html,txt"):
        """Enumerate directories over HTTPS"""
        cmd = f"gobuster dir -u https://{self.target} -w {wordlist} -x {extensions} -q -k"
        stdout, stderr = self._run_command(cmd)
        
        self.results["dir_enum_https"] = {
            "command": cmd,
            "output": stdout,
            "error": stderr if stderr else None
        }
        return self.results["dir_enum_https"]
    
    def enumerate_vhosts(self, wordlist="common.txt"):
        """Enumerate virtual hosts"""
        cmd = f"gobuster vhost -u http://{self.target} -w {wordlist} -q"
        stdout, stderr = self._run_command(cmd)
        
        self.results["vhost_enum"] = {
            "command": cmd,
            "output": stdout,
            "error": stderr if stderr else None
        }
        return self.results["vhost_enum"]
    
    def enumerate_dns(self, wordlist="common.txt", domain=None):
        """Enumerate DNS subdomains"""
        target_domain = domain if domain else self.target
        cmd = f"gobuster dns -d {target_domain} -w {wordlist} -q"
        stdout, stderr = self._run_command(cmd)
        
        self.results["dns_enum"] = {
            "command": cmd,
            "output": stdout,
            "error": stderr if stderr else None
        }
        return self.results["dns_enum"]
    
    def parse_results(self):
        """Parse Gobuster results"""
        parsed = {
            "directories": [],
            "status_codes": {}
        }
        
        for result in self.results.values():
            output = result.get("output", "")
            
            # Extract directories
            # Format: /path (Status: 200)
            lines = output.split('\n')
            for line in lines:
                line = line.strip()
                if '(Status:' in line:
                    # Extract path and status code
                    match = re.search(r'(.*?)\s+\(Status:\s+(\d+)\)', line)
                    if match:
                        path = match.group(1)
                        status = match.group(2)
                        parsed["directories"].append(path)
                        
                        if status not in parsed["status_codes"]:
                            parsed["status_codes"][status] = 0
                        parsed["status_codes"][status] += 1
        
        # Remove duplicates
        parsed["directories"] = list(set(parsed["directories"]))
        
        return parsed
