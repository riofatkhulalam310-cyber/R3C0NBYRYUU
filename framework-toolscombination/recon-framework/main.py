#!/usr/bin/env python3
"""
Reconnaissance Framework - Kali Linux Tools Combination
Combines: nmap, dig, nslookup, the_harvester, amass, gobuster
"""

import os
import sys
import argparse
import json
from datetime import datetime
from pathlib import Path

from modules.nmap_scanner import NmapScanner
from modules.dns_tools import DnsTools
from modules.harvester import HarvesterTools
from modules.amass_scanner import AmassScanner
from modules.gobuster_scanner import GobusterScanner


class ReconFramework:
    def __init__(self, target, output_dir="output"):
        self.target = target
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.report = {
            "target": target,
            "timestamp": self.timestamp,
            "results": {}
        }
        
    def run_nmap(self, scan_type="basic", ports="top1000"):
        """Run Nmap scan"""
        print(f"\n[*] Running Nmap scan on {self.target}...")
        scanner = NmapScanner(self.target)
        
        if scan_type == "basic":
            result = scanner.basic_scan(ports)
        elif scan_type == "aggressive":
            result = scanner.aggressive_scan()
        elif scan_type == "service":
            result = scanner.service_detection()
        else:
            result = scanner.basic_scan(ports)
            
        self.report["results"]["nmap"] = result
        print(f"[+] Nmap scan completed")
        return result
    
    def run_dns_enumeration(self):
        """Run DNS enumeration using dig and nslookup"""
        print(f"\n[*] Running DNS enumeration on {self.target}...")
        dns = DnsTools(self.target)
        
        results = {
            "dig": dns.run_dig(),
            "nslookup": dns.run_nslookup(),
            "dns_records": dns.enumerate_records()
        }
        
        self.report["results"]["dns"] = results
        print(f"[+] DNS enumeration completed")
        return results
    
    def run_harvester(self):
        """Run TheHarvester for email and subdomain enumeration"""
        print(f"\n[*] Running TheHarvester on {self.target}...")
        harvester = HarvesterTools(self.target)
        result = harvester.search()
        
        self.report["results"]["harvester"] = result
        print(f"[+] TheHarvester enumeration completed")
        return result
    
    def run_amass(self):
        """Run Amass for subdomain enumeration"""
        print(f"\n[*] Running Amass on {self.target}...")
        amass = AmassScanner(self.target)
        result = amass.enumerate()
        
        self.report["results"]["amass"] = result
        print(f"[+] Amass enumeration completed")
        return result
    
    def run_gobuster(self, wordlist="common.txt", extensions="php,html,txt"):
        """Run Gobuster for directory enumeration"""
        print(f"\n[*] Running Gobuster on {self.target}...")
        gobuster = GobusterScanner(self.target)
        result = gobuster.enumerate_directories(wordlist, extensions)
        
        self.report["results"]["gobuster"] = result
        print(f"[+] Gobuster enumeration completed")
        return result
    
    def run_full_recon(self, nmap_type="basic", wordlist="common.txt"):
        """Run full reconnaissance"""
        print(f"\n{'='*60}")
        print(f"[*] Starting Full Reconnaissance on {self.target}")
        print(f"{'='*60}\n")
        
        try:
            self.run_dns_enumeration()
            self.run_nmap(scan_type=nmap_type)
            self.run_harvester()
            self.run_amass()
            self.run_gobuster(wordlist=wordlist)
            
            self.save_report()
            print(f"\n{'='*60}")
            print(f"[+] Full Reconnaissance Completed!")
            print(f"[+] Report saved to: {self.get_report_path()}")
            print(f"{'='*60}\n")
            
        except Exception as e:
            print(f"[-] Error during reconnaissance: {str(e)}")
            sys.exit(1)
    
    def save_report(self):
        """Save reconnaissance report"""
        report_file = self.output_dir / f"recon_{self.target}_{self.timestamp}.json"
        with open(report_file, 'w') as f:
            json.dump(self.report, f, indent=4, default=str)
        print(f"[+] Report saved: {report_file}")
    
    def get_report_path(self):
        """Get the path to the latest report"""
        return self.output_dir / f"recon_{self.target}_{self.timestamp}.json"


def main():
    parser = argparse.ArgumentParser(
        description="Reconnaissance Framework - Kali Linux Tools Combination"
    )
    parser.add_argument("target", help="Target domain or IP address")
    parser.add_argument(
        "--mode",
        choices=["full", "dns", "nmap", "harvester", "amass", "gobuster"],
        default="full",
        help="Reconnaissance mode"
    )
    parser.add_argument(
        "--nmap-type",
        choices=["basic", "aggressive", "service"],
        default="basic",
        help="Nmap scan type"
    )
    parser.add_argument(
        "--wordlist",
        default="common.txt",
        help="Wordlist for Gobuster"
    )
    parser.add_argument(
        "--output",
        default="output",
        help="Output directory"
    )
    
    args = parser.parse_args()
    
    framework = ReconFramework(args.target, args.output)
    
    if args.mode == "full":
        framework.run_full_recon(args.nmap_type, args.wordlist)
    elif args.mode == "dns":
        framework.run_dns_enumeration()
        framework.save_report()
    elif args.mode == "nmap":
        framework.run_nmap(scan_type=args.nmap_type)
        framework.save_report()
    elif args.mode == "harvester":
        framework.run_harvester()
        framework.save_report()
    elif args.mode == "amass":
        framework.run_amass()
        framework.save_report()
    elif args.mode == "gobuster":
        framework.run_gobuster(wordlist=args.wordlist)
        framework.save_report()


if __name__ == "__main__":
    main()
