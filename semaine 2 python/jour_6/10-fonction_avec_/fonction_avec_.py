#!/usr/bin/env python3

"""exercice_10"""

__author__ = "skowro_j"


def greet(**kwargs) -> str:
    """Retourner un message formaté avec des arguments nommés."""
    name = kwargs.get("name")
    age = kwargs.get("age")
    return f"{name} a {age} ans."
