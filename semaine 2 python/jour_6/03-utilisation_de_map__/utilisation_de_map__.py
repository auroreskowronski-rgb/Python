#!/usr/bin/env python3

"""exercice_03"""

__author__ = "skowro_j"


def to_upper(words: list) -> list:
    """Appliquer une fonction de mise en majuscule à une liste de mots."""
    return list(map(str.upper, words))
