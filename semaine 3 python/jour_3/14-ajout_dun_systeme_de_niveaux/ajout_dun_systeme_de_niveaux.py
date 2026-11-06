#!/usr/bin/env python3

"""exercice_14"""

__author__ = "skowro_j"


class Personnage:
    """Classe représentant un personnage avec un nom
    des points de vie, une force et un niveau."""

    def __init__(self, nom: str, points_de_vie: int, force: int):
        """Définir une classe Personnage avec un nom
        des points de vie et une force."""
        self.nom = nom
        self.points_de_vie = points_de_vie
        self.force = force
        self.inventaire = []
        self.arme = None
        self.niveau = 1

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

    def ajouter_objet(self, objet: "Objet"):
        """Ajouter une méthode pour ajouter un objet à l’inventaire."""
        self.inventaire.append(objet)

    def equiper(self, arme: "Arme"):
        """Ajouter une méthode pour équiper une arme."""
        self.arme = arme
        for stat, value in arme.stats.items():
            if hasattr(self, stat):
                setattr(self, stat, getattr(self, stat) + value)

    def gagner_niveau(self):
        """Ajouter une méthode pour faire gagner un niveau au personnage."""
        self.niveau += 1
        self.points_de_vie += 10
        self.force += 10


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
        self.inventaire = []
        self.arme = None
        self.niveau = 1

    def lancer_sort(self, autre: Personnage, cout: int = 1) -> None:
        """lancer_sort() réduit les PV d’un ennemi et consomme du mana."""
        if self.mana >= cout:
            self.mana -= cout
            autre.points_de_vie -= cout * 2

    def gagner_niveau(self):
        """Ajouter une méthode pour faire gagner un niveau au personnage."""
        self.niveau += 1
        self.points_de_vie += 5
        self.mana += 5


class Objet:
    """Classe représentant un objet avec un nom
    un effet et des statistiques."""

    def __init__(self, nom: str, effet: str, stats: dict[str, int]):
        """Initialiser un objet avec un nom, un effet et des statistiques."""
        self.nom = nom
        self.effet = effet
        self.stats = stats

    def utiliser(self, personnage: "Personnage"):
        """Utiliser l'objet sur un personnage si c'est une potion."""
        if self.effet != "potion":
            return
        for stat, value in self.stats.items():
            if hasattr(personnage, stat):
                setattr(personnage, stat, getattr(personnage, stat) + value)


class Arme(Objet):
    """Classe représentant une arme avec un nom et des statistiques."""

    def __init__(self, nom: str, stats: dict[str, int]):
        """Initialiser une arme avec un nom et des statistiques."""
        self.nom = nom
        self.effet = "arme"
        self.stats = stats
