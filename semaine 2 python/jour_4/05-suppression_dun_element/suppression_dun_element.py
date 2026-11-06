#!/usr/bin/env python3

"""exercice_05"""

__author__ = "skowro_j"


def remove_element(lst: list, elem) -> list:
    """Supprimer un élément spécifique d'une liste (s'il existe)."""
    while elem in lst:
        lst.remove(elem)
    return lst
