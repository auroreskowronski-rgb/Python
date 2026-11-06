#!/usr/bin/env python3

"""exercice_03"""

__author__ = "skowro_j"


def add_entry(d: dict, key, value) -> dict:
    """Ajouter une paire clé-valeur à un dictionnaire existant. """
    d[key] = value
    return d
