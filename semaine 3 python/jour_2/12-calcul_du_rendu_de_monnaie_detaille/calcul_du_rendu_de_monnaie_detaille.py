#!/usr/bin/env python3

"""exercice_12"""

__author__ = "skowro_j"


def calculate_detailed_change(change: float) -> dict:
    """Donner le nombre de billets/pièces à rendre. """
    denominations = [
        500,
        200,
        100,
        50,
        20,
        10,
        5,
        2,
        1,
        0.5,
        0.2,
        0.1,
        0.05,
        0.02,
        0.01,
    ]
    detailed_change = {}
    for denom in denominations:
        count = int(change // denom)
        if count:
            detailed_change[str(denom)] = count
            change -= count * denom
            change = round(change, 2)
    return detailed_change
