"""
Daily Coding Problem: Problem #6 [Hard]
An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node. Implement an XOR linked list; it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python), you can assume you have access to get_pointer and dereference_pointer functions that converts between nodes and memory addresses.
"""

import unittest
import ctypes


def dereference_pointer(address):
    return ctypes.cast(
        address,
        ctypes.py_object
    ).value


def get_pointer(obj):
    return id(obj)


class Node(object):
    def __init__(self, value, both=None):
        self.value = value
        self.both = None


class XORLinkedList:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.length = 0
    
    def add(self, element):
        if self.length == 0:
            self.head.both = get_pointer(element)
            self.tail.both = get_pointer(element)
            element.both = get_pointer(self.head) ^ get_pointer(self.tail)
        else:
            prev = dereference_pointer(self.tail.both)
            prev_prev = prev.both ^ get_pointer(self.tail)
            prev.both = prev_prev ^ get_pointer(element)
            element.both = get_pointer(prev) ^ get_pointer(self.tail.both)
            self.tail.both = get_pointer(element) ^ 0
        self.length += 1
    
    def get(self, index):
        if index >= self.length:
            return None
        else:
            ptr = self.head.both
            prev_addr = get_pointer(self.head)

            for i in range(index):
                node = dereference_pointer(ptr)
                ptr = node.both ^ prev_addr
                prev_addr = ptr

            return dereference_pointer(ptr)


class Tests(unittest.TestCase):
    def test_example(self):
        n1, n2, n3 = Node('A'), Node('B'), Node('C')
        xor = XORLinkedList()
        xor.add(n1)
        xor.add(n2)
        xor.add(n3)
        self.assertEqual(
            xor.get(0).value,
            'A'
        )
        self.assertEqual(
            xor.get(1).value,
            'B'
        )
        self.assertEqual(
            xor.get(2).value,
            'C'
        )



if __name__ == '__main__':
    unittest.main()