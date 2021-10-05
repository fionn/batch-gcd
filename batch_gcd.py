#!/usr/bin/env python3
"""Batch GCD, FactHacks style"""

from math import prod, floor, gcd


def products(xs: list[int]) -> list[list[int]]:
    """Tree with the root as the product, input as leaves and intermediate
       states as intermediate nodes"""
    result = [xs]
    while len(xs) > 1:
        xs = [prod(xs[i * 2: (i + 1) * 2]) for i in range((len(xs) + 1) // 2)]
        result.append(xs)
    return result


def remainders(n: int, xs: list[int]) -> list[int]:
    """Compute n mod x_0, ..., n mod x_k in a batch"""
    tree = products(xs)
    result = [n]
    for node in reversed(tree):
        result = [result[floor(i / 2)] % node[i] for i in range(len(node))]
    return result


def batch_gcd(xs: list[int]) -> list[int]:
    """Batch GCD"""
    tree = products(xs)
    node = tree.pop()
    while tree:
        xs = tree.pop()
        node = [node[floor(i / 2)] % xs[i] ** 2 for i in range(len(xs))]
    return [gcd(r // n, n) for r, n in zip(node, xs)]


def main() -> None:
    """Entry point"""
    seq = [1909,2923,291,205,989,62,451,1943,1079,2419]
    b = batch_gcd(seq)
    print(b)


if __name__ == "__main__":
    main()
