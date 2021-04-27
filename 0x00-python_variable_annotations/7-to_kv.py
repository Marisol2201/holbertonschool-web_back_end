#!/usr/bin/env python3
"""type-annotated function to_kv"""

from typing import Tuple
import math


def to_kv(k: str, v: int) -> Tuple[str, int]:
    """type-annotated function to_kv that takes a string k and
    an int OR float v as arguments and returns a tuple. The first
    element of the tuple is the string k. The second element is
    the square of the int/float v and should be annotated as a float"""
    v = math.sqrt(v)
    return (k, v)
