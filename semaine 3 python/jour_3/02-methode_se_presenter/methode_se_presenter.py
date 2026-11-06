#!/usr/bin/env python3

"""exercice_02"""

__author__ = "skowro_j"


class Personnage:
    """Classe représentant un personnage avec un nom
    des points de vie et une force."""

    def __init__(self, nom: str, points_de_vie: int, force: int):
        """Définir une classe Personnage avec un nom
        des points de vie et une force."""
        self.nom = nom
        self.points_de_vie = points_de_vie
        self.force = force

    def se_presenter(self) -> str:
        """Ajouter une méthode pour
        afficher les infos du personnage."""
        return (
            f"Je suis {self.nom}, j'ai {self.points_de_vie} "
            f"points de vie et ma force est de {self.force}."
        )
