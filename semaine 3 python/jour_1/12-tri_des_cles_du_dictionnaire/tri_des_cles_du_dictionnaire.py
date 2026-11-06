#!/usr/bin/env python3

"""exercice_12"""

__author__ = "skowro_j"


def sort_dict_by_keys(d: dict) -> dict:
    """Trier le dictionnaire par ordre croissant des clés."""
    return dict(sorted(d.items()))
