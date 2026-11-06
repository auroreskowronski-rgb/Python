#!/usr/bin/env python3

"""exercice_05"""

__author__ = "skowro_j"


def is_palindrome(word: str) -> bool:
    """fonction qui retourne True si le mot est un palindrome, False sinon"""
    word = word.lower()
    return word == word[::-1]
