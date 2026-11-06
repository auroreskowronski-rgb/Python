#!/usr/bin/env python3

"""exercice_06"""

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

    def attaquer(self, autre: "Personnage") -> None:
        """Créer une méthode attaquer qui réduit la vie de l'adversaire"""
        autre.points_de_vie -= self.force

    def est_ko(self) -> bool:
        """Ajouter une méthode pour vérifier si le personnage est KO"""
        return self.points_de_vie <= 0


class Guerrier(Personnage):
    """Classe représentant un guerrier, qui est un type de personnage."""


class Mage(Personnage):
    """Classe représentant un mage
    qui est un type de personnage avec du mana."""

    def __init__(self, nom: str, points_de_vie: int, force: int, mana: int):
        """Spécialiser Personnage avec une classe Mage."""
        self.mana = mana
        self.nom = nom
        self.points_de_vie = points_de_vie
        self.force = force
