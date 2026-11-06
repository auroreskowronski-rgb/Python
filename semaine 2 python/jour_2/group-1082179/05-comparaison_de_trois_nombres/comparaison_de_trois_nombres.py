#!/usr/bin/env python3

"""exercice_05"""

__author__ = "skowro_j"


def max_of_three(a: int, b: int, c: int) -> int:
    """Retourne le plus grand des trois nombres."""
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
