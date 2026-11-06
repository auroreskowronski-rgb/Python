#!/usr/bin/env python3

"""exercice_16"""

__author__ = "skowro_j"


def sum_of_digits(n: int) -> int:
    """calcule la somme des chiffres d'un entier"""
    return sum(int(digit) for digit in str(abs(n)))


def factorial(n: int) -> int:
    """calcule la factorielle d'un entier"""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
