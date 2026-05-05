import os
import json
from src.detector import Detector
from src.scanner import Scanner
from src.reporter import Reporter
class LinuxVulnDetector:
def __init__(self, config_file):
self.config = json.load(open(config_file))
self.detector = Detector()
self.scanner = Scanner()
self.reporter = Reporter()
def run(self):
self.scanner.scan(self.config['kernel_version'])
self.detector.detect(self.scanner.results)
self.reporter.report(self.detector.results)
if __name__ == '__main__':
config_file = 'config.json'
detector = LinuxVulnDetector(config_file)
detector.run()