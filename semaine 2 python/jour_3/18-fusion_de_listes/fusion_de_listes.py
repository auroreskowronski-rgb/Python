#!/usr/bin/env python3

"""exercice_18"""

__author__ = "skowro_j"


def merge_lists(list1: list, list2: list) -> list:
    """fonction qui retourne une liste fusionnée à partir de deux listes"""

    return list(set(list1 + list2))
