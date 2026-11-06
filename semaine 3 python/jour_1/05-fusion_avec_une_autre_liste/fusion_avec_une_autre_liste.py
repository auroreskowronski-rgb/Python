#!/usr/bin/env python3

"""exercice_05"""

__author__ = "skowro_j"


def merge_lists(list1: list, list2: list) -> list:
    """Écrire une fonction qui retourne une list fusionnant deux listes
    de mêmes dimensions passées en paramètre.
    Les éléments des deux liste sont associée sous forme de tuples."""
    return [(list1[i], list2[i]) for i in range(len(list1))]
