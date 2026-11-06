#!/usr/bin/env python3

"""exercice_15"""

__author__ = "skowro_j"


def list_to_string(lst: list) -> str:
    """Convertir la liste triée en une chaîne de texte lisible."""
    return "\n".join(f"{i + 1}. {k}: {v}" for i, (k, v) in enumerate(lst))
