#!/usr/bin/env python3

"""exercice_10"""

__author__ = "skowro_j"


def grade_conversion(score: int) -> str:
    """Convertit un score en lettre selon l'échelle de notation."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
