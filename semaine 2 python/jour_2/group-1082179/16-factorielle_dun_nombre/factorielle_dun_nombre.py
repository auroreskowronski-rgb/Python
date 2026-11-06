#!/usr/bin/env python3

"""exercice_16"""

__author__ = "skowro_j"


def factorial(n: int) -> int:
    """Calcule la factorielle d'un nombre donné."""
    if n < 0:
        raise ValueError(
            "La factorielle n'est pas définie pour les nombres négatifs."
        )
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
