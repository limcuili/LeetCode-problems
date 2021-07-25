""" Symmetric Tree
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
Test with: python -m unittest symmetric_tree.py
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
    def isMirrored(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val == right.val:
            outward_pair = self.isMirrored(left.left, right.right)
            inward_pair = self.isMirrored(left.right, right.left)
            return outward_pair and inward_pair
        else:
            return False

    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.isMirrored(root.left, root.right)


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.tree_factory = TreeFactory()
        self.solution = Solution()

    def test_equivalent_tree(self):
        root = self.tree_factory.create([1,2,2,3,4,4,3])
        answer = self.solution.isSymmetric(root)
        self.assertTrue(answer)


if __name__ == 'main':
    unittest.main()
