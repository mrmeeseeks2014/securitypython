import sys
sys.path.append('c:\programming\git\securitypython\cyberprj2\python3-nmap')
import nmap3

nmap = nmap3.Nmap()

# Nmap Version
# results = nmap.nmap_version()

# Top Port Scan
# results = nmap.scan_top_ports("your-host")

# DNS-Brute-Script
# results = nmap.nmap_dns_brute_script("domain")

# Identify OS
# $ sudo nmap -O your-host.com
# os_results = nmap.nmap_os_detection("192.168.178.2") # MOST BE ROOT

# Identifying service version
# $ nmap 192.168.178.1  -sV
# version_result = nmap.nmap_version_detection("your-host.com")

