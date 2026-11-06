#!/usr/bin/env python3

"""exercice_13"""

__author__ = "skowro_j"


def remove_from_set(s: set, elem) -> set:
    """Supprimer un élément spécifique d'un ensemble."""
    s.discard(elem)
    return s
