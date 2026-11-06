#!/usr/bin/env python3

"""exercice_07"""

__author__ = "skowro_j"


def sum_recursive(n: int) -> int:
    """Calculer la somme des nombres jusqu'à n récursivement."""
    if n == 0:
        return 0
    return n + sum_recursive(n - 1)
