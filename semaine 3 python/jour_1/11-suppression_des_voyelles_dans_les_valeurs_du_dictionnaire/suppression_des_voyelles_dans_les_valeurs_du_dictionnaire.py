#!/usr/bin/env python3

"""exercice_11"""

__author__ = "skowro_j"


def remove_vowels_from_dict(d: dict) -> dict:
    """Modifier un dictionnaire pour supprimer
    toutes les entrées dont la clé commence par une voyelle."""
    vowels = "aeiouAEIOU"
    return {k: v for k, v in d.items() if not k[0] in vowels}
