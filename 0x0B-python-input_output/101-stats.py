#!/usr/bin/python3
"""Log parsing script."""
import sys

total_size = 0
codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
iteration = 0


def print_stats():
    """Function that prints a resume of the stats."""
    print("File size: {}".format(total_size))
    for k, v in sorted(codes.items()):
        if v is not 0:
            print("{}: {}".format(k, v))


try:
    for line in sys.stdin:
        line = line.split()

        codes[int(line[7])] += 1
        total_size += int(line[8])
        if iteration % 10 == 0 and iteration is not 0:
            print_stats()
        iteration += 1

except KeyboardInterrupt:
    print_stats()
    raise
