#!/usr/bin/env python3

"""exercice_14"""

__author__ = "skowro_j"


def dict_to_sorted_list(d: dict) -> list:
    """Transformer un dictionnaire en liste de
    tuples triée par valeurs décroissantes."""
    return sorted(d.items(), key=lambda item: item[1], reverse=True)
