#!/usr/bin/env python3
""" Functrion matrix_shape """


def matrix_shape(matrix):
    """ return the shape of a matrix """
    a = []
    while type(matrix) is not int:
        a.append(len(matrix))
        matrix = matrix[0]
    return a
