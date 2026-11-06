#!/usr/bin/env python3

"""exercice_15"""

__author__ = "skowro_j"


def add_to_list(item, lst=None) -> list:
    """Ajouter un élément à une liste (en gérant la mutabilité)."""
    if lst is None:
        lst = []
    lst.append(item)
    return lst
