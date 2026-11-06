#!/usr/bin/env python3

"""exercice_06"""

__author__ = "skowro_j"


def recursive_factorial(n: int) -> int:
    """fonction qui retourne la factorielle de n en utilisant la récursion"""
    if n <= 1:
        return 1
    else:
        return n * recursive_factorial(n - 1)
