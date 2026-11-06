#!/usr/bin/env python3

"""exercice_19"""

__author__ = "skowro_j"


def is_anagram(word1: str, word2: str) -> bool:
    """fonction qui retourne True si les deux mots
    sont des anagrammes, False sinon"""
    return sorted(word1.lower()) == sorted(word2.lower())
