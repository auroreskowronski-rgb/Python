#!/usr/bin/env python3

"""exercice_02"""

__author__ = "skowro_j"


def add_item(cart: list, name: str, price: float, quantity: int) -> list:
    """Ajouter un article sous forme de tuple (nom, prix, quantité)."""
    item = (name, price, quantity)
    cart.append(item)
    return cart
