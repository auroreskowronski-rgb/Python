#!/usr/bin/env python3

"""exercice_20"""

__author__ = "skowro_j"


def reverse_number(n: int) -> str:
    """Inverse les chiffres d'un nombre donné
    et retourne le résultat sous forme de chaîne."""
    if n == 0:
        return "0"  # Le nombre 0 inversé est toujours 0

    if n < 0:
        n = -n  # Convertir en positif si le nombre est négatif
        reversed_str = ""
        while n > 0:
            reversed_str += str(
                n % 10
            )  # Ajouter le dernier chiffre à la chaîne inversée
            n //= 10  # Enlever le dernier chiffre
        reversed_str = "-" + reversed_str  # Ajouter le signe négatif
        return reversed_str

    if n > 0:
        reversed_str = ""
        while n > 0:
            reversed_str += str(
                n % 10
            )  # Ajouter le dernier chiffre à la chaîne inversée
            n //= 10  # Enlever le dernier chiffre
        return reversed_str
