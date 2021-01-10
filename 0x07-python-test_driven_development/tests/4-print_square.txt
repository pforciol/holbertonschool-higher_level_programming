The ``print_square`` module
==========================

Using ``print_square``
---------------------

First import ``print_square`` from the ``print_square`` module:

	>>> print_square = __import__('4-print_square').print_square

Now use it:

	>>> print_square(0)

	>>> print_square(2)
	##
	##

	>>> print_square(2.0)
	Traceback (most recent call last):
	...
	TypeError: size must be an integer

	>>> print_square(None)
	Traceback (most recent call last):
	...
	TypeError: size must be an integer

	>>> print_square(-2)
	Traceback (most recent call last):
	...
	ValueError: size must be >= 0

	>>> print_square()
	Traceback (most recent call last):
		...
	TypeError: print_square() missing 1 required positional argument: 'size'
