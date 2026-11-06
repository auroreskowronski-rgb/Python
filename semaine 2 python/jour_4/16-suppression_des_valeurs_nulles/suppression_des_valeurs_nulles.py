#!/usr/bin/env python3

"""exercice_16"""

__author__ = "skowro_j"


def remove_none(lst: list) -> list:
    """Retirer tous les éléments None d'une liste."""
    lst2 = [element for element in lst if element is not None]
    return lst2
