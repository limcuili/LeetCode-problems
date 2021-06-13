""" Maximum Depth of Binary Tree
Given the root of a binary tree, return its maximum depth.
Test with: python -m unittest Maximum_Depth_of_Binary_Tree.py
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
        if index >= len(node_list) or node_list[index] is None:
            return None
        d = node_list[index]
        l = index * 2
        r = l + 1
        left_subtree = TreeFactory.create_tree_from_flat_list(node_list, l)
        right_subtree = TreeFactory.create_tree_from_flat_list(node_list, r)
        tree = TreeNode(d, left_subtree, right_subtree)
        return tree


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        return None


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.tree_factory = TreeFactory()
        self.solution = Solution()

    def test_empty(self):
        tree = self.tree_factory.create([])
        answer = self.solution.maxDepth(tree)
        expected_answer = 0
        self.assertEqual(expected_answer, answer)

    def test_root_only(self):
        tree = self.tree_factory.create([7])
        answer = self.solution.maxDepth(tree)
        expected_answer = 1
        self.assertEqual(expected_answer, answer)

    def test_with_empty_left(self):
        tree = self.tree_factory.create([1, None, 2])
        answer = self.solution.maxDepth(tree)
        expected_answer = 2
        self.assertEqual(expected_answer, answer)

    def test_three_levels(self):
        tree = self.tree_factory.create([3, 9, 20, 15, 7, None, None])
        answer = self.solution.maxDepth(tree)
        expected_answer = 3
        self.assertEqual(expected_answer, answer)