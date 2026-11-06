#!/usr/bin/env python3

"""exercice_19"""

import json

__author__ = "skowro_j"


def load_receipt_json(filename: str) -> list:
    """Charger et afficher un ticket depuis un fichier JSON. """
    with open(filename, "r") as f:
        return json.load(f)
