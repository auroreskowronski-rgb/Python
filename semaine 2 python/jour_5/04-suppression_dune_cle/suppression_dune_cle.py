#!/usr/bin/env python3

"""exercice_04"""

__author__ = "skowro_j"


def remove_key(d: dict, key) -> dict:
    """Supprimer une clé spécifique d'un dictionnaire."""
    if key in d:
        del d[key]
    return d
