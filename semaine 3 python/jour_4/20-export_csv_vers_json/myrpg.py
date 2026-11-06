#!/usr/bin/env python3

"""exercice_20"""

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

    def filtrer_plus_cher_que(self, prix: int) -> list[Item]:
        """Retourne une liste d'items dont
        le prix est supérieur au prix donné."""
        return [item for item in self.items_list if item.prix > prix]


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


def prix_achat(inventaire: Inventaire, list_achat: list[str]) -> int:
    """Calcule le coût total d'une liste
    d'achats donnée en utilisant l'inventaire."""
    total = 0
    for item_name in list_achat:
        prix = inventaire.recherche_prix(item_name)
        if prix == -1:
            continue
        total += prix
    return total


def valeur_inventaire(inventaire: Inventaire) -> int:
    """Calcule la valeur totale de l'inventaire."""
    total = 0
    for item in inventaire.items():
        total += item.prix
    return total


def exporter_inventaire(inventaire: Inventaire, fichier: str):
    """Exporte l'inventaire dans un fichier JSON."""
    with open(fichier, "w", newline="") as f:
        json.dump(
            {
                "items": [
                    {"nom": item.nom, "prix": item.prix}
                    for item in inventaire.items()
                ]
            },
            f,
            indent=4,
        )


def importer_inventaire(fichier: str):
    """Importe l'inventaire depuis un fichier JSON."""
    inventaire = Inventaire()
    if not os.path.exists(fichier):
        return Inventaire()
    with open(fichier, "r", newline="") as f:
        data = json.load(f)
    items = [Item(item["nom"], item["prix"]) for item in data.get("items", [])]
    inventaire = Inventaire()
    for item in items:
        inventaire.ajoute_item(item)
    return inventaire


def supprimer_objet_marche(nom_objet: str, fichier: str):
    """Supprime un objet du marché en le retirant du fichier CSV."""
    if not os.path.exists(fichier):
        return
    objets = lire_objets_marche(fichier)
    objets = [obj for obj in objets if obj[0] != nom_objet]
    with open(fichier, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["nom", "prix"])
        for nom, prix in objets:
            writer.writerow([nom, prix])


def ajouter_objets_en_lot(objets: list, fichier: str):
    """Ajoute plusieurs objets au marché en les ajoutant au fichier CSV."""
    if not os.path.exists(fichier):
        with open(fichier, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["nom", "prix"])
    with open(fichier, "a", newline="") as f:
        writer = csv.writer(f)
        for nom, prix in objets:
            writer.writerow([nom, prix])


def statistiques_marche(fichier: str) -> dict:
    """Retourne des statistiques sur le marché à partir du fichier CSV."""
    if not os.path.exists(fichier):
        return {"nombre_objets": 0, "prix_total": 0, "prix_moyen": 0}
    objets = lire_objets_marche(fichier)
    nombre_objets = len(objets)
    prix_total = sum(prix for _, prix in objets)
    prix_moyen = prix_total / nombre_objets if nombre_objets > 0 else 0
    return {"prix_moyen": prix_moyen, "nombre_object": nombre_objets}


def convertir_csv_en_json(fichier_csv: str, fichier_json: str):
    """Convertit un fichier CSV en fichier JSON."""
    if not os.path.exists(fichier_csv):
        return
    objets = lire_objets_marche(fichier_csv)
    data = {"items": [{"nom": nom, "prix": prix} for nom, prix in objets]}
    with open(fichier_json, "w", newline="") as f:
        json.dump(data, f, indent=4)
