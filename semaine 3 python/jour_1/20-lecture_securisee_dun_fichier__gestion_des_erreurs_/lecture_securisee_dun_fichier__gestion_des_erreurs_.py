#!/usr/bin/env python3

"""exercice_20"""

__author__ = "skowro_j"


def safe_read_file(filename: str) -> str:
    """Lire un fichier en capturant les erreurs potentielles"""
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        return "Erreur : fichier introuvable"
