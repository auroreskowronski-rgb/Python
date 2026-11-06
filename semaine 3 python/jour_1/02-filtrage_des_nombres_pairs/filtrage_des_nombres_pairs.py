#!/usr/bin/env python3

"""exercice_02"""

__author__ = "skowro_j"


def filter_even_numbers(numbers: list[int]) -> list:
    """Écrire une fonction qui retourne une liste constituée
    uniquement des nombres pairs contenus dans
    une liste passée en paramètre.z"""
    return [num for num in numbers if num % 2 == 0]
