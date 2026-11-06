#!/usr/bin/env python3

"""exercice_07"""

__author__ = "skowro_j"


def list_to_dict(pairs: list[tuple]) -> dict[int, str]:
    """Écrire une fonction qui prend une liste de paires en paramètre
    et retourne un dictionnaire (clé = nombre, valeur = lettre associée)."""
    return {pair[0]: pair[1] for pair in pairs}
