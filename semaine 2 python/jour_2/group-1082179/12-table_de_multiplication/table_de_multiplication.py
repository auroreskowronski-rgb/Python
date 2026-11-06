#!/usr/bin/env python3

"""exercice_12"""

__author__ = "skowro_j"


def multiplication_table(n: int) -> list:
    """Retourne la table de multiplication d'un nombre donné."""
    return [n * i for i in range(1, 11)]
