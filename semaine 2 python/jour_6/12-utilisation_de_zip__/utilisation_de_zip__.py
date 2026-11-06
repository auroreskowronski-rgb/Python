#!/usr/bin/env python3

"""exercice_12"""

__author__ = "skowro_j"


def pair_lists(list1: list, list2: list) -> list:
    """Associer deux listes élément par élément sous forme de tuples."""
    return list(zip(list1, list2))
