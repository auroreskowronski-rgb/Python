#!/usr/bin/env python3

"""exercice_18"""

__author__ = "skowro_j"

global_var = 0


def modify_global(value: int = 10) -> int:
    """Modifier une variable globale dans une fonction."""
    global global_var
    global_var = value
    return global_var
