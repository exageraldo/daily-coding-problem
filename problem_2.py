"""
Daily Coding Problem: Problem #2 [Hard]
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
Follow-up: what if you can't use division?
"""
import unittest
from functools import reduce 


def list_product_with_division(list_):
    aux_list = []
    prod = reduce((lambda x, y: x * y), list_)
    for num in list_:
        aux_list.append(prod//num)
    return aux_list


def list_product_without_division(list_):
    result = []
    for num in range(len(list_)):
        aux_list = list_[::]
        aux_list.pop(num)
        prod = reduce((lambda x, y: x * y), aux_list)
        result.append(prod)
    return result


class Tests(unittest.TestCase):
    def test_example_with_division(self):
        list_ = [1, 2, 3, 4, 5]
        expected = [120, 60, 40, 30, 24]
        self.assertEqual(
            list_product_with_division(list_),
            expected
        )
        list_ = [3, 2, 1]
        expected = [2, 3, 6]
        self.assertEqual(
            list_product_with_division(list_),
            expected
        )

    def test_example_without_division(self):
        list_ = [1, 2, 3, 4, 5]
        expected = [120, 60, 40, 30, 24]
        self.assertEqual(
            list_product_without_division(list_),
            expected
        )
        list_ = [3, 2, 1]
        expected = [2, 3, 6]
        self.assertEqual(
            list_product_without_division(list_),
            expected
        )

if __name__ == '__main__':
    unittest.main()