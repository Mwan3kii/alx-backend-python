#!/usr/bin/env python3
"""Return sum as float"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Takes a list of int and float"""
    return sum(mxd_lst)
