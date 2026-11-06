#!/usr/bin/env python3

"""exercice_17"""

__author__ = "skowro_j"


def solve_equation(a: float, b: float) -> float:
    """résout une équation du premier degré de la forme ax + b = 0"""
    if a == 0:
        raise ValueError("Le coefficient a ne peut pas être nul.")
    return -b / a
