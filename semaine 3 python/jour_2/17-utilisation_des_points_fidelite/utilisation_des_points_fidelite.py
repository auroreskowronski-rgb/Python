#!/usr/bin/env python3

"""exercice_17"""

__author__ = "skowro_j"


def redeem_loyalty_points(cart: list, points: int) -> float:
    """Permettre aux clients de payer avec leurs points fidélité."""
    total = sum(price * quantity for _, price, quantity in cart)
    discount = min(points, total)
    return round(total - discount, 2)
