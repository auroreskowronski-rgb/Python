#!/usr/bin/env python3

"""exercice_03"""

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
