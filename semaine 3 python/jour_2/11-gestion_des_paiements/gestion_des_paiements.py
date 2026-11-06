#!/usr/bin/env python3

"""exercice_11"""

__author__ = "skowro_j"


def process_payment(cart: list, amount_available: float, method: str) -> str:
    """Permettre un paiement par espèces ou carte."""
    total = 0
    for name, price, quantity in cart:
        total += price * quantity
    if method == "carte":
        if amount_available >= total:
            return "Paiement accepté par carte"
        else:
            return "Fonds insuffisants"
    elif method == "espèces":
        if amount_available >= total:
            return "Paiement accepté par espèces"
        else:
            return "Fonds insuffisants"
    else:
        return "Méthode de paiement non reconnue"
