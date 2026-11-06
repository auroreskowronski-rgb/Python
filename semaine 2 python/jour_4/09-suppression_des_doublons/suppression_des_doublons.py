#!/usr/bin/env python3

"""exercice_09"""

__author__ = "skowro_j"


def remove_duplicates(lst: list) -> list:
    """Retourner une liste sans doublons."""
    return list(dict.fromkeys(lst))
