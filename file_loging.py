import re  # Importing the 're' module for using regular expressions

# Path to the log file
log_file_path = r"C:\Users\Aadith\Desktop\Python automation\log analysis\log.txt"

# Lists to store extracted data
ip_addresses = []  
error_lines = []    
timestamp = []      

# Open the log file in read mode
with open(log_file_path, "r") as file:
    # Loop through each line in the file
    for line in file:
        # Search for an IP address using regex pattern (e.g., 192.168.1.1)
        ip_match = re.search(r'\b\d{1,3}(?:\.\d{1,3}){3}\b', line)
        if ip_match:
            ip_addresses.append(ip_match.group()) 

        # Search for a timestamp pattern (e.g., 2024-07-21 14:32:10)
        time_match = re.search(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', line)
        if time_match:
            timestamp.append(time_match.group())  # Add the matched timestamp to the list

        # If the line also contains "ERROR", store the entire line (stripped of spaces)
        if "ERROR" in line:
            error_lines.append(line.strip())

# Print extracted IP addresses
print("\nExtracted IP Addresses")
for ip in ip_addresses:
    print("  ->", ip)

# Print extracted timestamps
print("\nTimestamp:")
for ts in timestamp:
    print(" ->", ts)

# Print error lines
print("\nError Lines:")
for err in error_lines:
    print("  ->", err)

with open("extracted_ips.txt", "w") as f:
    for ip in ip_addresses:
        f.write(ip + "\n")

with open("timestamps.txt", "w") as f:
    for ts in timestamp:
        f.write(ts + "\n")

with open("errors.txt", "w") as f:
    for err in error_lines:
        f.write(err + "\n")
    
