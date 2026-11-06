#!/usr/bin/env python3

"""exercice_05"""

__author__ = "skowro_j"


def format_receipt(cart: list) -> str:
    """Générer un texte formaté affichant les articles et le total."""
    if not cart:
        return "Total : 0€"
    lines = []
    total = 0
    for name, price, quantity in cart:
        item_total = price * quantity
        total += item_total
        lines.append(f"{name} (x{quantity}) - {float(item_total)}€")
    lines.append(f"Total : {(float(total))}€")
    return "\n".join(lines)
