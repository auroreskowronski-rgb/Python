#!/usr/bin/env python3

"""exercice_14"""

__author__ = "skowro_j"


def is_prime(n: int) -> bool:
    """Vérifie si un nombre donné est premier."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
