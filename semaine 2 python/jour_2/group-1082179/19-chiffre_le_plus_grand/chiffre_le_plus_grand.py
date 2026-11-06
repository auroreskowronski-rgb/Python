#!/usr/bin/env python3

"""exercice_19"""

__author__ = "skowro_j"


def max_digit(n: int) -> int:
    """Retourne le chiffre le plus grand dans un nombre donné."""
    if n < 0:
        n = -n  # Convertir en positif si le nombre est négatif
    max_digit = 0
    while n > 0:
        digit = n % 10  # Obtenir le dernier chiffre
        if digit > max_digit:
            max_digit = digit  # Mettre à jour le chiffre maximum si nécessaire
        n //= 10  # Enlever le dernier chiffre
    return max_digit
