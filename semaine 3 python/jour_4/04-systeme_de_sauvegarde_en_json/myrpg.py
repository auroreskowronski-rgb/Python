#!/usr/bin/env python3

"""exercice_04"""

import json

__author__ = "skowro_j"


class Etre:
    """Classe représentant un personnage avec un nom
    des points de vie et une force."""

    def __init__(self, nom: str, points_de_vie: int):
        """Définir une classe Personnage avec un nom
        des points de vie et une force."""
        self.nom = nom
        self.points_de_vie = points_de_vie

    @property
    def force(self):
        """Retourne la force du personnage."""
        if not hasattr(self, "_force"):
            self._force = 0
        return self._force

    @force.setter
    def force(self, valeur):
        """Définit la force du personnage."""
        if not hasattr(self, "_force"):
            self._force = 0
        self._force = valeur


class Aventurier(Etre):
    """Classe représentant un aventurier, dérivée de la classe Etre."""


class Marchand(Etre):
    """Classe représentant un marchand, dérivée de la classe Etre."""


def sauvegarder_personnage(personnage: Etre, fichier: str):
    """Sauvegarde les informations d'un personnage dans un fichier JSON."""
    donnees = {
        "classe": personnage.__class__.__name__,
        "nom": personnage.nom,
        "points_de_vie": personnage.points_de_vie,
        "force": personnage.force,
    }
    with open(fichier, "w") as f:
        json.dump(donnees, f, indent=4)
