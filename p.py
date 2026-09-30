import csv
from collections import Counter
import os

filename = "malware_traffic.csv"

# Check whether the CSV file exists
if not os.path.isfile(filename):
    print(f"ERROR: File '{filename}' was not found.")
    print(f"Current directory: {os.getcwd()}")
    print("Place the CSV file in the same directory as p.py.")
    exit(1)

destination_ips = Counter()
destination_ports = Counter()
protocols = Counter()

with open(filename, "r", encoding="utf-8", errors="ignore", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        ip = row.get("Destination", "").strip()
        port = row.get("Destination Port", "").strip()
        protocol = row.get("Protocol", "").strip()

        if ip:
            destination_ips[ip] += 1

        if port:
            destination_ports[port] += 1

        if protocol:
            protocols[protocol] += 1

print("=== NETWORK BEHAVIOR ANALYSIS ===")

print("\nTop Destination IP Addresses:")
for ip, count in destination_ips.most_common(5):
    print(f"{ip} -> {count} packets")

print("\nTop Destination Ports:")
for port, count in destination_ports.most_common(5):
    print(f"{port} -> {count} packets")

print("\nProtocols Used:")
for protocol, count in protocols.most_common():
    print(f"{protocol} -> {count} packets")
