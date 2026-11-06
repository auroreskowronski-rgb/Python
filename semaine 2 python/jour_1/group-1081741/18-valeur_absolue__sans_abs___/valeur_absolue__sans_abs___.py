#!/usr/bin/env python3

"""exercice_18"""

__author__ = "skowro_j"


def absolute_value(n: int) -> int:
    """calcule la valeur absolue d'un entier sans utiliser la fonction abs()"""
    return n if n >= 0 else -n
