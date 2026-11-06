#!/usr/bin/env python3

"""exercice_13"""

__author__ = "skowro_j"


def merge_dicts(d1: dict, d2: dict) -> dict:
    """Fusionner deux dictionnaires en combinant
    leurs valeurs si les clés sont identiques."""
    merged = d1.copy()
    for k, v in d2.items():
        if k in merged:
            merged[k] += v
        else:
            merged[k] = v
    return merged
