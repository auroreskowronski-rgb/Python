#!/usr/bin/env python3

"""exercice_10"""

__author__ = "skowro_j"


def calculate_change(cart: list, amount_paid: float) -> float:
    """Calculer le rendu de monnaie après un paiement."""
    total = 0
    for name, price, quantity in cart:
        total += price * quantity
    return max(round(amount_paid - total, 2), 0.0)
