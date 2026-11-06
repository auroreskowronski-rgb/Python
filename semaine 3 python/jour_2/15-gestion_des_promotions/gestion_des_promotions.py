#!/usr/bin/env python3

"""exercice_15"""

__author__ = "skowro_j"


def apply_promotion(cart: list, promotions: dict) -> list:
    """Appliquer une réduction automatique sur certains articles."""
    for i, (item, price, quantity) in enumerate(cart):
        if item in promotions:
            discount = promotions[item] / 100
            cart[i] = (item, round(price * (1 - discount), 2), quantity)
    return cart
