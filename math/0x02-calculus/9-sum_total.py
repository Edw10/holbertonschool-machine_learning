#!/usr/bin/python3
""" Sum Total Function """


def summation_i_squared(n):
    """ summation_i_squared(n) function """
    if n >= 1:
        return int((n)*(n + 1)*(2*n + 1) / 6)
    return None
