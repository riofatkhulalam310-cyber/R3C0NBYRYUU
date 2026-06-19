#!/usr/bin/env python3
"""
Report Generator - Creates HTML reports from reconnaissance data
"""

import json
from datetime import datetime
from pathlib import Path


class ReportGenerator:
    def __init__(self, json_report_path):
        self.json_report_path = json_report_path
        self.report_data = self._load_json_report()
    
    def _load_json_report(self):
        """Load JSON report"""
        try:
            with open(self.json_report_path, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading report: {str(e)}")
            return None
    
    def generate_html(self, output_file=None):
        """Generate HTML report"""
        if not self.report_data:
            return None
        
        if output_file is None:
            output_file = self.json_report_path.replace('.json', '.html')
        
        html_content = self._build_html()
        
        with open(output_file, 'w') as f:
            f.write(html_content)
        
        return output_file
    
    def _build_html(self):
        """Build HTML content"""
        target = self.report_data.get('target', 'Unknown')
        timestamp = self.report_data.get('timestamp', 'Unknown')
        results = self.report_data.get('results', {})
        
        html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Reconnaissance Report - {target}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 20px;
            background-color: #f5f5f5;
        }}
        .header {{
            background-color: #333;
            color: white;
            padding: 20px;
            border-radius: 5px;
        }}
        .section {{
            background-color: white;
            margin: 20px 0;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }}
        .section h2 {{
            color: #333;
            border-bottom: 2px solid #007bff;
            padding-bottom: 10px;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 10px 0;
        }}
        table, th, td {{
            border: 1px solid #ddd;
        }}
        th {{
            background-color: #007bff;
            color: white;
            padding: 10px;
        }}
        td {{
            padding: 10px;
        }}
        tr:nth-child(even) {{
            background-color: #f2f2f2;
        }}
        .success {{
            color: green;
        }}
        .warning {{
            color: orange;
        }}
        .error {{
            color: red;
        }}
        pre {{
            background-color: #f4f4f4;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>Reconnaissance Report</h1>
        <p><strong>Target:</strong> {target}</p>
        <p><strong>Generated:</strong> {timestamp}</p>
    </div>
"""
        
        # DNS Results
        if 'dns' in results:
            html += self._build_dns_section(results['dns'])
        
        # Nmap Results
        if 'nmap' in results:
            html += self._build_nmap_section(results['nmap'])
        
        # TheHarvester Results
        if 'harvester' in results:
            html += self._build_harvester_section(results['harvester'])
        
        # Amass Results
        if 'amass' in results:
            html += self._build_amass_section(results['amass'])
        
        # Gobuster Results
        if 'gobuster' in results:
            html += self._build_gobuster_section(results['gobuster'])
        
        html += """
</body>
</html>
"""
        return html
    
    def _build_dns_section(self, dns_results):
        """Build DNS section"""
        html = '<div class="section"><h2>DNS Enumeration Results</h2>'
        
        if isinstance(dns_results, dict):
            for key, value in dns_results.items():
                if isinstance(value, dict) and 'output' in value:
                    html += f'<h3>{key.upper()}</h3><pre>{value["output"]}</pre>'
                elif isinstance(value, list):
                    html += f'<h3>{key.upper()}</h3><ul>'
                    for item in value:
                        html += f'<li>{item}</li>'
                    html += '</ul>'
        
        html += '</div>'
        return html
    
    def _build_nmap_section(self, nmap_results):
        """Build Nmap section"""
        html = '<div class="section"><h2>Nmap Scan Results</h2>'
        
        if isinstance(nmap_results, dict):
            for key, value in nmap_results.items():
                if isinstance(value, dict) and 'output' in value:
                    html += f'<h3>{key.replace("_", " ").title()}</h3><pre>{value["output"]}</pre>'
        
        html += '</div>'
        return html
    
    def _build_harvester_section(self, harvester_results):
        """Build TheHarvester section"""
        html = '<div class="section"><h2>TheHarvester Results</h2>'
        
        if isinstance(harvester_results, dict):
            for key, value in harvester_results.items():
                if isinstance(value, dict) and 'output' in value:
                    html += f'<h3>{key.replace("_", " ").title()}</h3><pre>{value["output"]}</pre>'
        
        html += '</div>'
        return html
    
    def _build_amass_section(self, amass_results):
        """Build Amass section"""
        html = '<div class="section"><h2>Amass Enumeration Results</h2>'
        
        if isinstance(amass_results, dict):
            for key, value in amass_results.items():
                if isinstance(value, dict) and 'output' in value:
                    html += f'<h3>{key.replace("_", " ").title()}</h3><pre>{value["output"]}</pre>'
        
        html += '</div>'
        return html
    
    def _build_gobuster_section(self, gobuster_results):
        """Build Gobuster section"""
        html = '<div class="section"><h2>Gobuster Directory Enumeration</h2>'
        
        if isinstance(gobuster_results, dict):
            for key, value in gobuster_results.items():
                if isinstance(value, dict) and 'output' in value:
                    html += f'<h3>{key.replace("_", " ").title()}</h3><pre>{value["output"]}</pre>'
        
        html += '</div>'
        return html


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python3 report_generator.py <json_report_path> [output_html]")
        sys.exit(1)
    
    json_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    generator = ReportGenerator(json_file)
    html_file = generator.generate_html(output_file)
    
    if html_file:
        print(f"[+] HTML report generated: {html_file}")
    else:
        print("[-] Failed to generate HTML report")
