#!/usr/bin/env python3

"""exercice_13"""

__author__ = "skowro_j"


def is_triangle(a: int, b: int, c: int) -> bool:
    """Vérifie si trois longueurs peuvent former un triangle."""
    return a + b > c and a + c > b and b + c > a
