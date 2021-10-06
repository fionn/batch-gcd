#!/usr/bin/env python3
"""Batch GCD, FactHacks style"""

from math import prod, floor, gcd
from collections.abc import Sequence


name = "batch-gcd" # pylint: disable=invalid-name
__title__ = name
__version__ = "0.0.1"


def products(xs: Sequence[int]) -> list[Sequence[int]]:
    """Tree with the root as the product, input as leaves and intermediate
       states as intermediate nodes"""
    result = [xs]
    while len(xs) > 1:
        xs = [prod(xs[i * 2: (i + 1) * 2]) for i in range((len(xs) + 1) // 2)]
        result.append(xs)
    return result


def remainders(n: int, xs: Sequence[int]) -> list[int]:
    """Compute n mod x_0, ..., n mod x_k in a batch"""
    tree = products(xs)
    result = [n]
    for node in reversed(tree):
        result = [result[floor(i / 2)] % node[i] for i in range(len(node))]
    return result


def batch_gcd(xs: Sequence[int]) -> list[int]:
    """Batch GCD"""
    tree = products(xs)
    node = tree.pop()
    while tree:
        xs = tree.pop()
        node = [node[floor(i / 2)] % xs[i] ** 2 for i in range(len(xs))]
    return [gcd(r // n, n) for r, n in zip(node, xs)]
