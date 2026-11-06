#!/usr/bin/env python3

"""exercice_10"""

__author__ = "skowro_j"


def squares(lst: list) -> list:
    """Retourner une liste contenant les carrés des nombres donnés."""
    square_lst = []
    for element in lst:
        square_lst.append(element**2)
    return square_lst
