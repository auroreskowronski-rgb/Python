#!/usr/bin/env python3

"""exercice_04"""

__author__ = "skowro_j"


def is_leap_year(year: int) -> bool:
    """Détermine si une année est bissextile."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
