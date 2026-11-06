#!/usr/bin/env python3

"""exercice_06"""

__author__ = "skowro_j"


def save_receipt(filename: str, content: str):
    """Sauvegarder le ticket dans un fichier ticket.txt."""
    with open(filename, "w") as file:
        file.write(content)
