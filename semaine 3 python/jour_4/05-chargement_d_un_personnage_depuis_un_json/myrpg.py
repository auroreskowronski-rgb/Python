#!/usr/bin/env python3

"""exercice_05"""

import json
import os

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


def charger_personnage(fichier: str) -> Etre | None:
    """Charge les informations d'un personnage depuis un fichier JSON."""
    if not os.path.exists(fichier):
        return None
    elif os.path.exists(fichier):
        try:
            with open(fichier, "r") as f:
                donnees = json.load(f)
            classe = donnees.get("classe")
            nom = donnees.get("nom")
            points_de_vie = donnees.get("points_de_vie")
            force = donnees.get("force", 0)
            if classe == "Aventurier":
                personnage = Aventurier(nom, points_de_vie)
            elif classe == "Marchand":
                personnage = Marchand(nom, points_de_vie)
            else:
                return None
            personnage.force = force
            return personnage
        except (json.JSONDecodeError, KeyError, TypeError):
            return None
