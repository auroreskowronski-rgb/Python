#!/usr/bin/env python3

"""exercice_14"""

__author__ = "skowro_j"


def bitwise_operations(a: int, b: int) -> tuple:
    """effectue les opérations bit à bit sur deux entiers"""
    return (a & b, a | b, a ^ b)
