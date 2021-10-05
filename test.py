#!/usr/bin/env python3
"""Unit tests"""

import unittest

from batch_gcd import products, remainders, batch_gcd

class TestFactHack(unittest.TestCase):
    """FactHack test cases"""

    def test_product_tree_small_sequence(self) -> None:
        """Calculate a product tree"""
        seq = [10, 20, 30, 40, 50, 60]
        tree = products(seq)
        self.assertEqual(tree, [[10, 20, 30, 40, 50, 60], [200, 1200, 3000],
                                [240000, 3000], [720000000]])

    def test_remainder_tree_small_sequence(self) -> None:
        """Calculate a remainder tree"""
        tree = remainders(8675309, [11, 13, 17, 19, 23])
        self.assertEqual(tree, [5, 6, 5, 4, 8])

    def test_batch_gcd_small_sequence(self) -> None:
        """Perform batch GCD on a small sequence"""
        seq = [1909, 2923, 291, 205, 989, 62, 451, 1943, 1079, 2419]
        gs = batch_gcd(seq)
        self.assertEqual(gs, [1909, 1, 1, 41, 23, 1, 41, 1, 83, 41])


if __name__ == "__main__":
    unittest.main(verbosity=2, buffer=True)
