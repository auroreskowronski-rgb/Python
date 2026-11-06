#!/usr/bin/env python3

"""exercice_14"""

__author__ = "skowro_j"


def update_stock(stock: dict, cart: list) -> dict:
    """Déduire les articles achetés du stock disponible."""
    for item, _, quantity in cart:
        if item in stock:
            stock[item] -= quantity
            if stock[item] < 0:
                stock[item] = 0
    return stock
