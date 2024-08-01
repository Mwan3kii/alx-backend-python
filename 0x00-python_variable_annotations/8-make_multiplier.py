#!/usr/bin/env python3
"""Type annotated function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Takes float argument returns multiples of float"""
    def multiplier_function(value: float) -> float:
        return value * multiplier
    return multiplier_function
