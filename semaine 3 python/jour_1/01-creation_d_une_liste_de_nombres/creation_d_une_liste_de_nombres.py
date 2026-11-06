#!/usr/bin/env python3

"""exercice_01"""

__author__ = "skowro_j"


def create_list(n: int) -> list:
    """Écrire une fonction qui retourne une
    liste contenant les nombres de 1 à n."""
    if n > 0:
        return list(range(1, n + 1))
    else:
        return []
