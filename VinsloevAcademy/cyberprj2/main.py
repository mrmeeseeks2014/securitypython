import sys
sys.path.append('c:\programming\git\securitypython\cyberprj2\python3-nmap')
import nmap3

nmap = nmap3.Nmap()

# Nmap Version
# results = nmap.nmap_version()

# Version Detection
# results = nmap.nmap_version_detection("your-host") # Must be root

# Top Port Scan
# results = nmap.scan_top_ports("your-host")

# List Scan
# results = nmap.nmap_list_scan("your-host")

# Subnet Scan
# results = nmap.nmap_subnet_scan("your-host") #Must be root

# DNS-Brute-Script
# results = nmap.nmap_dns_brute_script("domain")

# Identify OS
# $ sudo nmap -O your-host.com
# os_results = nmap.nmap_os_detection("192.168.178.2") # MOST BE ROOT

# Identifying service version
# $ nmap 192.168.178.1  -sV
# version_result = nmap.nmap_version_detection("your-host.com")

### Scanning Commands ###

# FIN Scan
# result = nmap.nmap_fin_scan("192.168.178.1")

# Idle Scann
# result = nmap.nmap_idle_scan("192.168.178.1")

# Ping Scan
# result = nmap.nmap_ping_scan("192.168.178.1")

# SYN Scan
# result = nmap.nmap_syn_scan("192.168.178.1")

# TCP Scan
# result = nmap.nmap_tcp_scan("192.168.178.1")

# UDP Scan
# result = nmap.nmap_udp_scan("192.168.178.1")

### Host Discovery ###

# results = nmap.nmap_portscan_only("your-host")
# results = nmap.nmap_no_portscan("your-host")
# results = nmap.nmap_arp_discovery("your-host")
# results = nmap.nmap_disable_dns("your-host")

### Custom Nmap Commands ###

# results = nmap.scan_top_ports("host", args="-sV")

### Vulners Script identify CVEs ###

# ressults = nmap_version_detection("host", args="--script vulners --script-args mincvss+5.0")
