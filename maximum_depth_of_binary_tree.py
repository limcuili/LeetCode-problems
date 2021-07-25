""" Maximum Depth of Binary Tree
Given the root of a binary tree, return its maximum depth.
Test with: python -m unittest maximum_depth_of_binary_tree.py
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
    def maxDepth1(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def maxDepth2(self, root: TreeNode) -> int:
        # DFS implementation
        if root is None:
            return 0

        max_depth = 1
        node_stack = [root]
        levels = [1]

        while node_stack:
            current_node = node_stack.pop()
            level = levels.pop()

            if current_node.left is None and current_node.right is None:
                max_depth = max(max_depth, level)

            if current_node.right is not None:
                node_stack.append(current_node.right)
                levels.append(level + 1)

            if current_node.left is not None:
                node_stack.append(current_node.left)
                levels.append(level + 1)

        return max_depth

    def maxDepth3(self, root: TreeNode) -> int:
        # TODO: BFS queue
        return None

    def maxDepth(self, root: TreeNode) -> int:
        # hook in whichever of the above implementation you want.
        return self.maxDepth2(root)


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
