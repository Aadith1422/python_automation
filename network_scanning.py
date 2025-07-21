import os
import platform
import csv

# Function to check if a host is reachable
def is_host_up(ip):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    
    # Build ping command based on OS
    if platform.system().lower() == "windows":
        command = f"ping {param} 1 {ip} >nul 2>&1"
    else:
        command = f"ping {param} 1 {ip} > /dev/null 2>&1"
    
    return os.system(command) == 0  # Returns True if host responds

# Path to CSV file containing IP addresses
csv_file_path = r"c:\Users\Aadith\Desktop\Python automation\network scanning\IP.csv"

# Lists to store scan results
active_hosts = []
inactive_hosts = []

print("[*] Reading IPs from CSV and scanning...\n")

# Read each IP from CSV and check status
with open(csv_file_path, "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        ip = row['IP'].strip()
        if ip:
            if is_host_up(ip):
                print(f"[+] Host {ip} is UP")
                active_hosts.append(ip)
            else:
                print(f"[-] Host {ip} is DOWN")
                inactive_hosts.append(ip)

# Print final summary
print("\nScan Complete.")
print(f"\nActive Hosts: {len(active_hosts)}")
for host in active_hosts:
    print(f"  -> {host}")

print(f"\nInactive Hosts: {len(inactive_hosts)}")
for host in inactive_hosts:
    print(f"  -> {host}")
