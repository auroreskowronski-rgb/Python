#!/usr/bin/env python3

"""exercice_06"""

__author__ = "skowro_j"


def factorial(n: int) -> int:
    """Implémenter une fonction récursive pour
    calculer la factorielle d’un nombre."""
    if n == 0:
        return 1
    return n * factorial(n - 1)
