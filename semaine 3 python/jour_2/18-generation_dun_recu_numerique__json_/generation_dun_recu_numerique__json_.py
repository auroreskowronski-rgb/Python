#!/usr/bin/env python3

"""exercice_18"""

import json

__author__ = "skowro_j"


def save_receipt_json(filename: str, cart: list):
    """Sauvegarder le ticket en JSON pour usage digital."""
    receipt = [
        {"name": item, "price": price, "quantity": quantity}
        for item, price, quantity in cart
    ]
    with open(filename, "w") as f:
        json.dump(receipt, f, indent=4)
