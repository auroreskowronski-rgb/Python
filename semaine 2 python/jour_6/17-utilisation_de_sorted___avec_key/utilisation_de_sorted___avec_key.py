#!/usr/bin/env python3

"""exercice_17"""

__author__ = "skowro_j"


def sort_tuples(lst: list) -> list:
    """Trier une liste de tuples par leur deuxième élément."""
    return sorted(lst, key=lambda x: x[1])
