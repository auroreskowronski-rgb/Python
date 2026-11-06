#!/usr/bin/env python3

"""exercice_09"""

__author__ = "skowro_j"


def invert_dict(d: dict) -> dict:
    """Inverser les clés et les valeurs d'un dictionnaire"""
    return {v: k for k, v in d.items()}
