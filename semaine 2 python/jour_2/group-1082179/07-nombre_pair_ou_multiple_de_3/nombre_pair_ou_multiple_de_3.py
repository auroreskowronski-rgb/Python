#!/usr/bin/env python3

"""exercice_07"""

__author__ = "skowro_j"


def check_number(n: int) -> str:
    """Détermine si un nombre est pair ou multiple de 3."""
    if n % 3 == 0:
        return "multiple de 3"
    elif n % 2 == 0:
        return "pair"
    else:
        return "rien de spécial"
