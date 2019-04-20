"""
Daily Coding Problem: Problem #4 [Hard]
Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
You can modify the input array in-place.
"""

import unittest

def positive_integer_missing(list_):
    max_int = max(list_)
    aux_list = range(1, max_int+2)
    list_ = [item for item in list_ if item > 0]
    set_diff = set(aux_list) - set(list_)
    return min(set_diff)


class Tests(unittest.TestCase):
    def test_example(self):
        list_ = [3, 4, -1, 1]
        expected = 2
        self.assertEqual(
            positive_integer_missing(list_),
            expected
        )
        list_ = [1, 2, 0]
        expected = 3
        self.assertEqual(
            positive_integer_missing(list_),
            expected
        )


if __name__ == '__main__':
    unittest.main()