#!/usr/bin/env python3

"""exercice_09"""

__author__ = "skowro_j"


def product_sign(a: int, b: int) -> str:
    """Détermine le signe du produit de deux nombres."""
    product = a * b
    if product > 0:
        return "positif"
    elif product < 0:
        return "négatif"
    else:
        return "nul"
