#!/usr/bin/env python3

"""exercice_15"""

__author__ = "skowro_j"


def sum_of_digits(n: int) -> int:
    """calcule la somme des chiffres d'un entier"""
    return sum(int(digit) for digit in str(abs(n)))
