#!/usr/bin/env python3
"""
Nmap Scanner Module
"""

import subprocess
import json
import re


class NmapScanner:
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
                timeout=300
            )
            return result.stdout, result.stderr
        except subprocess.TimeoutExpired:
            return "", "Command timed out"
        except Exception as e:
            return "", str(e)
    
    def basic_scan(self, ports="top1000"):
        """Basic Nmap scan"""
        cmd = f"nmap -p- --top-ports {ports} {self.target}"
        stdout, stderr = self._run_command(cmd)
        
        self.results["basic_scan"] = {
            "command": cmd,
            "output": stdout,
            "error": stderr if stderr else None
        }
        return self.results["basic_scan"]
    
    def aggressive_scan(self):
        """Aggressive Nmap scan with OS detection"""
        cmd = f"nmap -A -T4 {self.target}"
        stdout, stderr = self._run_command(cmd)
        
        self.results["aggressive_scan"] = {
            "command": cmd,
            "output": stdout,
            "error": stderr if stderr else None
        }
        return self.results["aggressive_scan"]
    
    def service_detection(self):
        """Service and version detection"""
        cmd = f"nmap -sV -sC {self.target}"
        stdout, stderr = self._run_command(cmd)
        
        self.results["service_detection"] = {
            "command": cmd,
            "output": stdout,
            "error": stderr if stderr else None
        }
        return self.results["service_detection"]
    
    def udp_scan(self):
        """UDP port scan"""
        cmd = f"nmap -sU --top-ports 100 {self.target}"
        stdout, stderr = self._run_command(cmd)
        
        self.results["udp_scan"] = {
            "command": cmd,
            "output": stdout,
            "error": stderr if stderr else None
        }
        return self.results["udp_scan"]
    
    def parse_results(self):
        """Parse Nmap results"""
        parsed = {
            "open_ports": [],
            "services": []
        }
        
        for result in self.results.values():
            output = result.get("output", "")
            # Extract open ports
            ports = re.findall(r'(\d+)/tcp\s+open\s+(\S+)', output)
            for port, service in ports:
                parsed["open_ports"].append({
                    "port": port,
                    "service": service
                })
        
        return parsed
