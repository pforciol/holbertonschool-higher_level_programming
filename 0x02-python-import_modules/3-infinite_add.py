#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    ac = len(sys.argv) - 1
    res = 0

    if ac > 0:
        for i in range(ac):
            res += int(sys.argv[i + 1])
    print("{:d}".format(res))
