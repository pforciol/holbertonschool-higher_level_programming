#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    ac = len(sys.argv) - 1

    print("{:d} argument{:s}{:s}"
          .format(ac, 's' if ac != 1 else '', ':' if ac != 0 else '.'))
    if ac > 0:
        for i in range(ac):
            print("{:d}: {:s}".format(i + 1, sys.argv[i + 1]))
