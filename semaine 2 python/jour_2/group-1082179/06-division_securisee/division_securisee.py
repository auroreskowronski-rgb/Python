#!/usr/bin/env python3

"""exercice_06"""

__author__ = "skowro_j"


def safe_divide(a: int, b: int) -> float:
    """Effectue une division sécurisée en évitant la division par zéro."""
    if b == 0:
        return "Erreur : division par zéro"
    return a / b
