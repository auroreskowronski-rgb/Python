#!/usr/bin/env python3

"""exercice_19"""

__author__ = "skowro_j"


def fibonacci(n: int) -> int:
    """Retourner le n-ième terme de la suite de Fibonacci."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
