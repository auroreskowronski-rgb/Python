#!/usr/bin/env python3

"""exercice_20"""

__author__ = "skowro_j"


def sales_statistics(sales_data: list) -> dict:
    """Calculer les statistiques de ventes à partir des données de ventes."""
    statistics = {}
    for item, quantity in sales_data:
        if item in statistics:
            statistics[item] += quantity
        else:
            statistics[item] = quantity

    return statistics
