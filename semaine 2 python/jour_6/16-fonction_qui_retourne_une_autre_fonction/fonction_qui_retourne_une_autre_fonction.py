#!/usr/bin/env python3

"""exercice_16"""

__author__ = "skowro_j"


def make_power(n: int):
    """Retourner une fonction qui élève à une puissance donnée."""

    def power(x: int) -> int:
        """Élever x à la puissance n."""
        return x**n

    return power
