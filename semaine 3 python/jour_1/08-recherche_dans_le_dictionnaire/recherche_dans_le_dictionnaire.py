#!/usr/bin/env python3

"""exercice_08"""

__author__ = "skowro_j"


def get_value_from_dict(d: dict, key: int) -> str:
    """Vérifier si une clé est présente dans le
    dictionnaire et retourner sa valeur"""
    return d.get(key, "Clé non trouvée")
