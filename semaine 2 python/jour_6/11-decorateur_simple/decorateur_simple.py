#!/usr/bin/env python3

"""exercice_11"""

__author__ = "skowro_j"


def debug(func):
    """Créer un décorateur qui affiche "Début" et "Fin"
    autour d’un appel de fonction."""

    def wrapper():
        """Affiche 'Début' avant l'appel de la fonction et 'Fin' après."""
        print("Début")
        result = func()
        print("Fin")
        return result

    return wrapper
