#!/usr/bin/env python3

"""exercice_08"""

__author__ = "skowro_j"


def apply_discount(cart: list, discount: float) -> float:
    """Appliquer un pourcentage de remise sur le total."""
    total = 0
    for name, price, quantity in cart:
        total += price * quantity
    return round(total * (1 - discount / 100), 2)
