#!/usr/bin/env python3

"""exercice_12"""

__author__ = "skowro_j"


def is_prime_optimized(n: int) -> bool:
    """fonction qui retourne True si n est un nombre premier, False sinon"""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
