The ``text_indentation`` module
==========================

Using ``text_indentation``
---------------------

First import ``text_indentation`` from the ``text_indentation`` module:

	>>> text_indentation = __import__('5-text_indentation').text_indentation

Now use it:

	>>> text_indentation("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quonam modo? Utrum igitur tibi: litteram videor an totas paginas commovere")
	Lorem ipsum dolor sit amet, consectetur adipiscing elit.
	<BLANKLINE>
	Quonam modo?
	<BLANKLINE>
	Utrum igitur tibi:
	<BLANKLINE>
	litteram videor an totas paginas commovere

	>>> text_indentation("Lorem:")
	Lorem:
	<BLANKLINE>

	>>> text_indentation("Betty")
	Betty

	>>> text_indentation(":Betty")
	:
	<BLANKLINE>
	Betty

	>>> text_indentation(":")
	:
	<BLANKLINE>

	>>> text_indentation(":.")
	:
	<BLANKLINE>
	.
	<BLANKLINE>

	>>> text_indentation(" ")

	>>> text_indentation("")

	>>> text_indentation(" .")
	.
	<BLANKLINE>

	>>> text_indentation(-2)
	Traceback (most recent call last):
	...
	TypeError: text must be a string

	>>> text_indentation(None)
	Traceback (most recent call last):
	...
	TypeError: text must be a string
