#!/usr/bin/env python3

"""exercice_13"""

__author__ = "skowro_j"


def check_stock(stock: dict, item: str, quantity: int) -> bool:
    """Vérifier si un article est encore disponible en stock."""
    return stock.get(item, 0) >= quantity
