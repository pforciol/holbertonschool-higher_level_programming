#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if (number < 0):
    nb = ((-number) % 10) * -1
else:
    nb = number % 10
print("Last digit of {:d} is {:d} and is".format(number, nb), end='')
if (nb > 5):
    print(" greater than 5")
elif (nb == 0):
    print(" 0")
else:
    print(" less than 6 and not 0")
