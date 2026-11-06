#!/usr/bin/env python3

"""exercice_14"""

__author__ = "skowro_j"


def even_numbers(lst: list) -> list:
    """Retourner uniquement les nombres pairs d'une liste."""
    even_lst = []
    for element in lst:
        if element % 2 == 0:
            even_lst.append(element)
    return even_lst
