#!/usr/bin/env python3

"""exercice_06"""

__author__ = "skowro_j"


def merge_dicts(d1: dict, d2: dict) -> dict:
    """Retourner la fusion de deux dictionnaires."""
    merged = d1.copy()
    merged.update(d2)
    return merged
