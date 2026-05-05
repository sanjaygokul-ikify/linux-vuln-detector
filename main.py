import os
import json
from src.detector import Detector
from src.scanner import Scanner
from src.reporter import Reporter

class LinuxVulnDetector:
    def __init__(self, config_file):
        # Open and parse the configuration file
        with open(config_file, 'r') as f:
            self.config = json.load(f)
            
        self.detector = Detector()
        self.scanner = Scanner()
        self.reporter = Reporter()
        
    def run(self):
        # 1. Scan the kernel
        self.scanner.scan(self.config.get('kernel_version', 'latest'))
        
        # 2. Detect vulnerabilities
        self.detector.detect(self.scanner.results)
        
        # 3. Report findings
        self.reporter.report(self.detector.results)

if __name__ == '__main__':
    config_file = 'config.json'
    detector = LinuxVulnDetector(config_file)
    detector.run()
