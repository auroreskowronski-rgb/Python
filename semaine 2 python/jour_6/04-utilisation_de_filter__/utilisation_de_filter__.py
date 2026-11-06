#!/usr/bin/env python3

"""exercice_04"""

__author__ = "skowro_j"


def filter_even(numbers: list) -> list:
    """Filtrer les nombres pairs d’une liste."""
    return list(filter(lambda x: x % 2 == 0, numbers))
