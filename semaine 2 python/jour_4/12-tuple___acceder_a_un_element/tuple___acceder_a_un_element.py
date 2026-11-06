#!/usr/bin/env python3

"""exercice_12"""

__author__ = "skowro_j"


def get_tuple_element(tpl: tuple, index: int):
    """Retourner l’élément d’un tuple à l’index donné."""
    if index > len(tpl) - 1 or index < 0:
        return
    element = tpl[index]
    return element
