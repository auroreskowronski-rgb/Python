#!/usr/bin/env python3

"""exercice_16"""

__author__ = "skowro_j"


def calculate_loyalty_points(cart: list) -> int:
    """Générer des points fidélité en fonction du total."""
    total = sum(price * quantity for _, price, quantity in cart)
    return int(total)
