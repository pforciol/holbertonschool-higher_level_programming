#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 100 + 1):
        if i % 3 == 0 or i % 5 == 0:
            if i % 3 == 0:
                print("Fizz", end='')
            if i % 5 == 0:
                print("Buzz", end='')
        else:
            print("{:d}".format(i), end='')
        print(" ", end='')
