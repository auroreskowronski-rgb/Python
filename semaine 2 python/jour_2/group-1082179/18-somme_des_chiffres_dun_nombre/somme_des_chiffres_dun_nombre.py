#!/usr/bin/env python3

"""exercice_18"""

__author__ = "skowro_j"


def sum_of_digits(n: int) -> int:
    """Calcule la somme des chiffres d'un nombre donné."""
    if n < 0:
        n = -n  # Convertir en positif si le nombre est négatif
    total = 0
    while n > 0:
        total += n % 10  # Ajouter le dernier chiffre à la somme
        n //= 10  # Enlever le dernier chiffre
    return total
