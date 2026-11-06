#!/usr/bin/env python3

"""exercice_10"""

__author__ = "skowro_j"


def count_char_occurrences(d: dict, char: str) -> int:
    """Compter le nombre d'occurrences d'un caractère donné
    dans toutes les valeurs d'un dictionnaire."""
    return sum(str(value).count(char) for value in d.values())
