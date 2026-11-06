#!/usr/bin/env python3

"""exercice_15"""

__author__ = "skowro_j"


def sum_up_to(n: int) -> int:
    """Calcule la somme des entiers de 1 à n."""
    if n < 1:
        return 0
    return (n * (n + 1)) // 2
