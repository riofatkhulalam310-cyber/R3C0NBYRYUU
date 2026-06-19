#!/usr/bin/env python3
"""
DNS Tools Module - dig and nslookup
"""

import subprocess
import re


class DnsTools:
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
                timeout=30
            )
            return result.stdout, result.stderr
        except subprocess.TimeoutExpired:
            return "", "Command timed out"
        except Exception as e:
            return "", str(e)
    
    def run_dig(self):
        """Run dig command"""
        cmd = f"dig {self.target} +short"
        stdout, stderr = self._run_command(cmd)
        
        self.results["dig"] = {
            "command": cmd,
            "output": stdout,
            "error": stderr if stderr else None
        }
        return self.results["dig"]
    
    def run_dig_full(self):
        """Run full dig command"""
        cmd = f"dig {self.target}"
        stdout, stderr = self._run_command(cmd)
        
        self.results["dig_full"] = {
            "command": cmd,
            "output": stdout,
            "error": stderr if stderr else None
        }
        return self.results["dig_full"]
    
    def run_nslookup(self):
        """Run nslookup command"""
        cmd = f"nslookup {self.target}"
        stdout, stderr = self._run_command(cmd)
        
        self.results["nslookup"] = {
            "command": cmd,
            "output": stdout,
            "error": stderr if stderr else None
        }
        return self.results["nslookup"]
    
    def enumerate_records(self):
        """Enumerate DNS records (A, MX, NS, TXT)"""
        records = {}
        record_types = ["A", "MX", "NS", "TXT", "CNAME", "SOA"]
        
        for rtype in record_types:
            cmd = f"dig {self.target} {rtype} +short"
            stdout, stderr = self._run_command(cmd)
            records[rtype] = stdout.strip().split('\n') if stdout else []
        
        self.results["dns_records"] = records
        return records
    
    def reverse_lookup(self, ip):
        """Reverse DNS lookup"""
        cmd = f"dig -x {ip} +short"
        stdout, stderr = self._run_command(cmd)
        
        self.results["reverse_lookup"] = {
            "ip": ip,
            "output": stdout,
            "error": stderr if stderr else None
        }
        return self.results["reverse_lookup"]
    
    def zone_transfer(self):
        """Attempt DNS zone transfer"""
        # Get nameservers first
        cmd = f"dig {self.target} NS +short"
        stdout, stderr = self._run_command(cmd)
        nameservers = stdout.strip().split('\n') if stdout else []
        
        zone_transfer_results = {}
        
        for ns in nameservers:
            if ns:
                cmd = f"dig @{ns} {self.target} axfr"
                stdout, stderr = self._run_command(cmd)
                zone_transfer_results[ns] = {
                    "output": stdout,
                    "error": stderr if stderr else None
                }
        
        self.results["zone_transfer"] = zone_transfer_results
        return zone_transfer_results
    
    def parse_results(self):
        """Parse DNS results"""
        parsed = {
            "ips": [],
            "nameservers": [],
            "mx_records": [],
            "txt_records": []
        }
        
        # Extract IPs from dig output
        if "dig" in self.results:
            output = self.results["dig"].get("output", "")
            ips = re.findall(r'(\d+\.\d+\.\d+\.\d+)', output)
            parsed["ips"] = list(set(ips))
        
        # Extract nameservers
        if "dns_records" in self.results:
            ns_records = self.results["dns_records"].get("NS", [])
            parsed["nameservers"] = ns_records
            mx_records = self.results["dns_records"].get("MX", [])
            parsed["mx_records"] = mx_records
            txt_records = self.results["dns_records"].get("TXT", [])
            parsed["txt_records"] = txt_records
        
        return parsed
