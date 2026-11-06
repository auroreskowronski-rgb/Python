#!/usr/bin/env python3

"""exercice_01"""

__author__ = "skowro_j"


def create_list(n: int) -> list:
    """Créer une liste"""
    list1 = []
    if n == 0:
        return list1
    if n < 0:
        i = -1
        while i in range(0, n - 1, -1):
            list1 += [i]
            i -= 1
        return list1

    if n > 0:
        i = 1
        while i in range(n + 1):
            list1 += [i]
            i += 1
        return list1
    return []
