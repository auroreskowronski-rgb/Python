#!/usr/bin/env python3

"""exercice_09"""

__author__ = "skowro_j"


def add_vat(cart: list, vat: float) -> float:
    """Ajouter un taux de TVA au total."""
    total = 0
    for name, price, quantity in cart:
        total += price * quantity
    return round(total * (1 + vat / 100), 2)
