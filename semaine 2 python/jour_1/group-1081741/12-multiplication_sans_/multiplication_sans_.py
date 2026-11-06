#!/usr/bin/env python3

"""exercice_12"""

__author__ = "skowro_j"


def multiply(a: int, b: int) -> int:
    """fais une multiplication"""
    res = 0
    for i in range(0, abs(b)):
        res += a
    if b < 0:
        res = -res
    return res
