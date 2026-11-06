#!/usr/bin/env python3

"""exercice_04"""

__author__ = "skowro_j"


def replace_multiples_of_3(numbers: list[int]) -> list:
    """
    Écrire une fonction qui prend en paramètre une liste
    et retourne une liste en remplaçant chaque multiple de 3 par "Fizz".

    """
    return ["Fizz" if num % 3 == 0 else num for num in numbers]
