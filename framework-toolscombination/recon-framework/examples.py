#!/usr/bin/env python3
"""
Quick Start Examples
"""

import subprocess
import sys

def run_example(description, command):
    """Run an example"""
    print(f"\n{'='*60}")
    print(f"[*] {description}")
    print(f"{'='*60}")
    print(f"Command: {command}\n")
    
    response = input("Run this example? (y/n): ")
    if response.lower() == 'y':
        subprocess.run(command, shell=True)


def main():
    print("Reconnaissance Framework - Quick Start Examples\n")
    
    target = input("Enter target domain (e.g., example.com): ").strip()
    if not target:
        print("No target specified")
        sys.exit(1)
    
    examples = [
        ("DNS Enumeration", f"python3 main.py {target} --mode dns"),
        ("Basic Nmap Scan", f"python3 main.py {target} --mode nmap"),
        ("Aggressive Nmap Scan", f"python3 main.py {target} --mode nmap --nmap-type aggressive"),
        ("TheHarvester Reconnaissance", f"python3 main.py {target} --mode harvester"),
        ("Amass Subdomain Enumeration", f"python3 main.py {target} --mode amass"),
        ("Gobuster Directory Scan", f"python3 main.py {target} --mode gobuster"),
        ("Full Reconnaissance", f"python3 main.py {target} --mode full"),
    ]
    
    for i, (description, command) in enumerate(examples, 1):
        print(f"\n{i}. {description}")
    
    print(f"\n{len(examples) + 1}. Exit")
    
    while True:
        try:
            choice = int(input("\nSelect an example (1-7): "))
            if 1 <= choice <= len(examples):
                run_example(examples[choice-1][0], examples[choice-1][1])
            elif choice == len(examples) + 1:
                print("Exiting...")
                sys.exit(0)
            else:
                print("Invalid selection")
        except KeyboardInterrupt:
            print("\n\nInterrupted")
            sys.exit(0)
        except ValueError:
            print("Invalid input")


if __name__ == "__main__":
    main()
