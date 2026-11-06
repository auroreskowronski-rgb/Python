#!/usr/bin/env python3

"""exercice_16"""

__author__ = "skowro_j"


def write_to_file(filename: str, content: str):
    """Sauvegarder la chaîne formatée dans un fichier texte."""
    with open(filename, "w") as f:
        f.write(content)
