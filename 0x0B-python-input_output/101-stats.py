#!/usr/bin/python3
"""Log parsing script."""
import sys
import signal

total_size = 0
codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
iteration = 1


def print_stats():
    print("File size: {}".format(total_size))
    for k, v in sorted(codes.items()):
        if v is not 0:
            print("{}: {}".format(k, v))


def signal_handler(sig, frame):
    """Signal handler function."""
    print_stats()
    sys.exit()


for line in sys.stdin:
    line = line.split()
    if iteration % 10 == 0:
        print_stats()

    codes[int(line[7])] += 1
    total_size += int(line[8])

    iteration += 1
    signal.signal(signal.SIGINT, signal_handler)
