#!/usr/bin/env python3

"""exercice_07"""

__author__ = "skowro_j"


def load_receipt(filename: str) -> str:
    """Lire et afficher un ticket précédemment sauvegardé."""
    with open(filename, "r") as file:
        return file.read()
