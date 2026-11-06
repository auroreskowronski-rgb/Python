#!/usr/bin/env python3

"""exercice_04"""

__author__ = "skowro_j"


def calculate_total(cart: list) -> float:
    """Retourner le total du panier en tenant compte des quantités."""
    total = sum(price * quantity for _, price, quantity in cart)
    return float(round(total, 2))
