"""
Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.
For example, given the following Node class
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:
node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
"""
import unittest

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(node):
    def _serialize(node_):
        string_node = []
        if isinstance(node_, Node):
            string_node.append(node_.val)
            string_node += _serialize(node_.right)
            string_node += _serialize(node_.left)
        else:
            string_node.append('NaN') # Not A Node
        return string_node

    serialized_list = _serialize(node)
    return '_'.join(str(s) for s in serialized_list)


def deserialize(string_node):
    def _deserialize(list_node_):
        value = list_node_.pop(0)
        if value == 'NaN':
            node_ = Node(None)
        else:
            node_ = Node(value)
            node_.right = _deserialize(list_node_)
            node_.left = _deserialize(list_node_)
        return node_
    
    list_node = string_node.split('_')
    deserialized = _deserialize(list_node)
    return deserialized


class Tests(unittest.TestCase):
    def test_example(self):
        node = Node(
            'root',
            Node('left', Node('left.left')),
            Node('right')
        )
        expected = 'left.left'
        
        self.assertEqual(
            deserialize(serialize(node)).left.left.val,
            expected
        )


if __name__ == '__main__':
    unittest.main()