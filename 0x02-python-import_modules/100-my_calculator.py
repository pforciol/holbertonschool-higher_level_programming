#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    av = sys.argv
    ac = len(av) - 1

    if ac != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if av[2] not in "+-*/":
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    fcts = {'+': add, '-': sub, '*': mul, '/': div}
    print("{:s} {:s} {:s} = {:d}".format(av[1], av[2], av[3],
                                         fcts[av[2]](int(av[1]), int(av[3]))))
