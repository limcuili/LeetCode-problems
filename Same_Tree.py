""" Same Tree
Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Test with: python -m unittest Same_Tree.py
"""

import unittest
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TreeFactory:
    def create(self, source: List[int]) -> TreeNode:
        return TreeFactory.create_tree_from_flat_list([None] + source)

    @staticmethod
    def create_tree_from_flat_list(node_list, index=1):
        if index >= len(node_list) or node_list[index] is None: return None
        d = node_list[index]
        l = index * 2
        r = l + 1
        left_subtree = TreeFactory.create_tree_from_flat_list(node_list, l)
        right_subtree = TreeFactory.create_tree_from_flat_list(node_list, r)
        tree = TreeNode(d, left_subtree, right_subtree)
        return tree


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not q or not p:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.tree_factory = TreeFactory()
        self.solution = Solution()

    def test_equivalent_tree(self):
        p = self.tree_factory.create([1, 2, 3])
        q = self.tree_factory.create([1, 2, 3])
        answer = self.solution.isSameTree(p, q)
        self.assertTrue(answer)


if __name__ == 'main':
    unittest.main()
