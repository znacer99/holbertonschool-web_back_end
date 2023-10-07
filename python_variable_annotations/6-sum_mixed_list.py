#!/usr/bin/env python3
"""
a type annotated function
"""
from typing import Union, List

def sum_mixed_list(mxd_lst: list[Union[int, float]]) -> float:
    """
    sum every item in a list
    """
    return sum(mxd_lst)
