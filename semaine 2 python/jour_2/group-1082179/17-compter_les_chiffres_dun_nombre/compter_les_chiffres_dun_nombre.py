#!/usr/bin/env python3

"""exercice_17"""

__author__ = "skowro_j"


def count_digits(n: int) -> int:
    """Compte le nombre de chiffres dans un nombre donné."""
    if n < 0:
        n = -n  # Convertir en positif si le nombre est négatif
    if n == 0:
        return 1  # Le nombre 0 a un chiffre
    count = 0
    while n > 0:
        n //= 10  # Diviser par 10 pour enlever le dernier chiffre
        count += 1
    return count
