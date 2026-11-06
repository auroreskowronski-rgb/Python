#!/usr/bin/env python3

"""exercice_05"""

__author__ = "skowro_j"


from functools import reduce


def product(numbers: list) -> int:
    """Calculer le produit de tous les éléments d’une liste."""
    return reduce(lambda x, y: x * y, numbers, 1)
