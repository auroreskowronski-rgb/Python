#!/usr/bin/env python3

"""exercice_18"""

import os

__author__ = "skowro_j"


def delete_file_if_contains(filename: str, word: str):
    """Supprimer le fichier texte si son contenu
    contient un mot spécifique.."""
    try:
        with open(filename, "r") as f:
            content = f.read()
        if word in content:
            os.remove(filename)
    except FileNotFoundError:
        pass
