#!/usr/bin/python3
"""Log parsing script."""
import sys


def print_stats(total_size, codes):
    print("File size: {}".format(total_size))
    for k, v in sorted(codes.items()):
        if v is not 0:
            print("{}: {}".format(k, v))


total_size = 0
codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
iteration = 0
try:
    for line in sys.stdin:
        if iteration % 10 == 0 and iteration is not 0:
            print_stats(total_size, codes)

        codes[int(line.split(' ')[7])] += 1
        total_size += int(line.split(' ')[8])

        iteration += 1

except KeyboardInterrupt:
    print_stats(total_size, codes)
