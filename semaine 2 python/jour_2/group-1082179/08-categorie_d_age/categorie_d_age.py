#!/usr/bin/env python3

"""exercice_08"""

__author__ = "skowro_j"


def age_category(age: int) -> str:
    """Retourne la catégorie d'âge en fonction de l'âge donné."""
    if age < 12:
        return "enfant"
    elif age < 18:
        return "ado"
    elif age < 70:
        return "adulte"
    else:
        return "senior"
