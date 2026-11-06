#!/usr/bin/env python3

"""exercice_11"""

__author__ = "skowro_j"


def day_of_week(n: int) -> str:
    """Retourne le jour de la semaine correspondant à un nombre donné."""
    days = {
        1: "lundi",
        2: "mardi",
        3: "mercredi",
        4: "jeudi",
        5: "vendredi",
        6: "samedi",
        7: "dimanche",
    }
    return days.get(n, "Erreur, nombre invalide")
