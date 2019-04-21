"""
Daily Coding Problem: Problem #5 [Medium]
cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.
Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

Implement car and cdr.
"""

import unittest


def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


def car(pair):
    _f = lambda a, b: a
    return pair(_f)


def cdr(pair):
    _f = lambda a, b: b
    return pair(_f)


class Tests(unittest.TestCase):
    def test_example(self):
        self.assertEqual(
            car(cons(3, 4)),
            3
        )
        self.assertEqual(
            cdr(cons(3, 4)),
            4
        )


if __name__ == '__main__':
    unittest.main()