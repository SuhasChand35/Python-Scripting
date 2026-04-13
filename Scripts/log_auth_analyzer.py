from collections import defaultdict

log = "access.log"

failed = defaultdict(int)

with open(log, "r") as file:
    for line in file:
        parts = line.split()
        
        ip = parts[0]
        status = parts[-1]
        
        if status == "401":
            failed[ip] += 1

print("Failed Login Attempts:")
for ip, count in failed.items():
    print(f"{ip} → {count} failed attempts")
