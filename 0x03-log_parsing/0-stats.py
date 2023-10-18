#!/usr/bin/python3
""" A script that reads stdin line by line and computes metrics."""

import sys

stats = {'200': 0, '301': 0, '400': 0, '401': 0,
         '403': 0, '404': 0, '405': 0, '500': 0}
total_size = 0
line_count = 0

try:
    for line in sys.stdin:
        parts = line.split(" ")
        if len(parts) > 4:
            code = parts[-2]
            size = int(parts[-1])
            if code in stats.keys():
                stats[code] += 1
            total_size += size
            line_count += 1

        if line_count == 10:
            line_count = 0
            print('File size: {}'.format(total_size))
            for key, value in sorted(stats.items()):
                if value != 0:
                    print('{}: {}'.format(key, value))

except Exception as err:
    pass

finally:
    print('File size: {}'.format(total_size))
    for key, value in sorted(stats.items()):
        if value != 0:
            print('{}: {}'.format(key, value))
