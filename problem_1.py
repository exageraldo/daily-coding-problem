"""
Daily Coding Problem: Problem #1 [Easy]
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
Bonus: Can you do this in one pass?
"""

from itertools import combinations
import unittest


def sum_two_items(list_, k):
    all_possib = combinations(list_, 2)
    for possib in all_possib:
        if sum(possib) == k:
            return True
    return False


class Tests(unittest.TestCase):
    def test_example(self):
        list_ = [10, 15, 3, 7]
        k = 17
        self.assertTrue(
            sum_two_items(list_, 17)
        )

if __name__ == '__main__':
    unittest.main()