#!/usr/bin/env python3

"""exercice_13"""

__author__ = "skowro_j"


def is_palindrome(s: str) -> bool:
    """vérifie si une chaîne de caractères est un palindrome"""
    s = s.replace(" ", "").lower()
    return s == s[::-1]
