#!/usr/bin/env python3

"""exercice_03"""

__author__ = "skowro_j"


def sum_numbers(numbers: list) -> int:
    """Écrire une fonction qui prend en paramètre une liste
    et retourne la somme des nombres contenu dans la liste."""
    return sum(numbers)


def sum_even_numbers(numbers: list) -> int:
    """Écrire une fonction qui prend en paramètre une liste
    et retourne la somme des nombres pairs contenu dans la liste."""
    return sum(num for num in numbers if num % 2 == 0)
