#!/usr/bin/env python3

"""exercice_03"""

__author__ = "skowro_j"


def remove_item(cart: list, name: str) -> list:
    """Retirer un article du panier par son nom."""
    cart = [item for item in cart if item[0] != name]
    return cart
