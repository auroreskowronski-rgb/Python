#!/usr/bin/env python3

"""exercice_17"""

__author__ = "skowro_j"


def contains(lst: list, elem) -> bool:
    """Vérifier si un élément existe dans une liste."""
    i = 0
    for element in lst:
        if element is elem:
            i += 1
    return i >= 1
