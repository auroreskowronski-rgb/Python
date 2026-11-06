#!/usr/bin/env python3

"""exercice_11"""

import csv
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


class Item:
    """Classe représentant un objet avec un nom et un prix."""

    def __init__(self, nom: str, prix: int):
        """Initialise un objet Item avec un nom et un prix."""
        self.nom = nom
        self.prix = prix

    def __repr__(self) -> str:
        """Retourne une représentation en chaîne
        de caractères de l'objet Item."""
        return f"Item(nom={self.nom}, prix={self.prix})"


class Inventaire:
    """Classe représentant un inventaire d'objets."""

    def __init__(self):
        """Initialiser un inventaire vide."""
        self.items_list = []

    def ajoute_item(self, item: "Item"):
        """Ajoute un item donné à l'inventaire."""
        self.items_list.append(item)

    def retire_item(self, item: "Item"):
        """Retire un item donné à l'inventaire. Pas d'erreur si
        l'item est absent."""
        if item in self.items_list:
            self.items_list.remove(item)

    def items(self):
        """Retourne la liste des items actuellement dans
        l'inventaire."""
        return self.items_list

    def charger_depuis_csv(self, fichier: str):
        """Remplace les items de l'inventaire par
        ceux du fichier CSV passé en paramètre."""
        if not os.path.exists(fichier):
            return
        with open(fichier, "r", newline="") as f:
            reader = csv.DictReader(f)
            self.items_list = [
                Item(row["nom"], int(row["prix"])) for row in reader
            ]

    def sauver_en_csv(self, fichier: str):
        """Sauvegarde l'inventaire dans le fichier
        CSV passé en paramètre, en remplaçant son contenu."""
        with open(fichier, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["nom", "prix"])
            for item in self.items_list:
                writer.writerow([item.nom, item.prix])

    def recherche_prix(self, item_name) -> int:
        """Recherche le prix d'un item par son nom.
        Retourne le prix si trouvé, sinon -1."""
        for item in self.items_list:
            if item.nom == item_name:
                return item.prix
        return -1


def ajouter_object_marche(nom: str, prix: int, fichier: str):
    """Ajoute un objet au marché en l'écrivant dans un fichier CSV."""
    if not os.path.exists(fichier):
        with open(fichier, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["nom", "prix"])
    with open(fichier, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([nom, prix])


def lire_objets_marche(fichier: str) -> list[tuple[str, int]]:
    """Lit les objets du marché depuis un fichier CSV
    et retourne une liste de tuples (nom, prix)."""
    objets = []
    if not os.path.exists(fichier):
        return objets
    with open(fichier, "r", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            nom = row.get("nom")
            prix = int(row.get("prix", 0))
            objets.append((nom, prix))
    return objets
