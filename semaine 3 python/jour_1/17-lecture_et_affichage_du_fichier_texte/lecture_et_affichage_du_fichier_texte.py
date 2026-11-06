#!/usr/bin/env python3

"""exercice_17"""

__author__ = "skowro_j"


def read_from_file(filename: str) -> str:
    """Lire le fichier texte et afficher son contenu."""
    with open(filename, "r") as f:
        return f.read()
