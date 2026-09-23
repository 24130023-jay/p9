import csv
from collections import Counter
filename = "malware_traffic.csv"
destination_ips = Counter()
destination_ports = Counter()
protocols = Counter()
with open(filename, "r", encoding="utf-8", errors="ignore") as file:
    reader = csv.DictReader(file)

    for row in reader:
        ip = row.get("Destination", "")
        port = row.get("Destination Port", "")
        protocol = row.get("Protocol", "")
        if ip:
            destination_ips[ip] += 1
        if port:
            destination_ports[port] += 1
        if protocol:
            protocols[protocol] += 1
print("=== NETWORK BEHAVIOR ANALYSIS ===")
print("\nTop Destination IP Addresses:")
for ip, count in destination_ips.most_common(5):
    print(ip, "->", count, "packets")

print("\nTop Destination Ports:")
for port, count in destination_ports.most_common(5):
    print(port, "->", count, "packets")

print("\nProtocols Used:")
for protocol, count in protocols.most_common():
    print(protocol, "->", count, "packets")
