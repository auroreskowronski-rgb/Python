#!/usr/bin/env python3

"""exercice_15"""

__author__ = "skowro_j"


def filter_even(numbers: list) -> list:
    """fonction qui retourne une liste contenant
    uniquement les nombres pairs d'une liste"""
    return [num for num in numbers if num % 2 == 0]
