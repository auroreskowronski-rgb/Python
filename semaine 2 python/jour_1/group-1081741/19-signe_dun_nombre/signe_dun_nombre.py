#!/usr/bin/env python3

"""exercice_19"""

__author__ = "skowro_j"


def sign(n: int) -> int:
    """calcule le signe d'un entier sans utiliser la fonction sign()"""
    return 0 if n == 0 else (1 if n > 0 else -1)
