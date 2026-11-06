#!/usr/bin/env python3

"""exercice_08"""

__author__ = "skowro_j"


def make_adder(x: int):
    """Retourner une fonction qui ajoute un nombre donné à son paramètre."""

    def adder(y: int) -> int:
        return x + y

    return adder
