#!/usr/bin/env python3

"""exercice_03"""

__author__ = "skowro_j"


def number_sign(n: int) -> str:
    """Détermine si un nombre est positif, négatif ou nul."""
    if n > 0:
        return "positif"
    elif n < 0:
        return "négatif"
    else:
        return "nul"
