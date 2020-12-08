#!/usr/bin/python3
for i in range(0, 99 + 1):
    if (i == 99):
        print("{:2d}".format(i))
    else:
        print("{:02d}, ".format(i), end='')
