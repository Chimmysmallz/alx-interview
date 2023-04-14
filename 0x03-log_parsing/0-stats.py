#!/usr/bin/python3

import sys
from collections import defaultdict

total_size = 0
status_codes = defaultdict(int)
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()
        if len(parts) != 7:
            continue
        ip, _, _, _, status, size, _ = parts
        if not status.isdigit():
            continue
        status = int(status)
        if status not in status_codes:
            status_codes[status] = 0
        status_codes[status] += 1
        total_size += int(size)
        if line_count % 10 == 0:
            print(f"Total file size: {total_size}")
            for code in sorted(status_codes.keys()):
                print(f"{code}: {status_codes[code]}")
            print()
except KeyboardInterrupt:
    print("Interrupted by user")

print(f"Total file size: {total_size}")
for code in sorted(status_codes.keys()):
    print(f"{code}: {status_codes[code]}")
