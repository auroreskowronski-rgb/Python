#!/usr/bin/env python3

"""
exercice_02
concatener deux chaines
"""

__author__ = "skowro_j"


def convert_type(value):
    """Convertir une string en int et vice versa"""
    if isinstance(value, str):
        return int(value)
    if isinstance(value, int):
        return str(value)
