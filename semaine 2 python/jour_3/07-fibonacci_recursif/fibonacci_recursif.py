#!/usr/bin/env python3

"""exercice_07"""

__author__ = "skowro_j"


def fibonacci(n: int) -> int:
    """fonction qui retourne le n-ième nombre de Fibonacci en utilisant
    la récursion"""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
