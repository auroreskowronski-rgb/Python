#!/usr/bin/env python3

"""exercice_20"""

__author__ = "skowro_j"


def sort_three_numbers(a: int, b: int, c: int) -> tuple:
    """trie trois nombres sans utiliser la fonction sort()"""
    if a > b:
        a, b = b, a
    if a > c:
        a, c = c, a
    if b > c:
        b, c = c, b
    return a, b, c
