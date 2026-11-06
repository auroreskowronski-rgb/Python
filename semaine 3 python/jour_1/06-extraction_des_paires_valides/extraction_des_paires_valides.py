#!/usr/bin/env python3

"""exercice_06"""

__author__ = "skowro_j"


def extract_valid_pairs(pairs: list) -> list:
    """Écrire une fonction qui retourne une liste
    ne contenant que les paires dont le premier élément
    est un nombre entier d'une liste passée en paramètre."""
    return [pair for pair in pairs if isinstance(pair[0], int)]
