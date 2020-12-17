#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    return set_1 ^ set_2
# The symmetrical difference of A and B, denoted “A Δ B”
# (read “A delta B”) is the set of elements which belong
# either to A or to B, but not to both at the same time.
# We can use set_1.symetric_difference(set_2) too.
