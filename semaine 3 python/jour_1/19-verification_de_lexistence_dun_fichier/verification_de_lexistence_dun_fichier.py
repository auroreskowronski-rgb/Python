#!/usr/bin/env python3

"""exercice_19"""

import os

__author__ = "skowro_j"


def file_exists(filename: str) -> bool:
    """Vérifier si un fichier texte existe."""
    return os.path.isfile(filename)
