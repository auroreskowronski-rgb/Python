#!/usr/bin/env python3

"""exercice_20"""

__author__ = "skowro_j"


def count_occurrences(lst: list, elem) -> int:
    """Retourner le nombre d’occurrences d’un élément dans une liste."""
    i = 0
    for element in lst:
        if element is elem:
            i += 1
    return i
