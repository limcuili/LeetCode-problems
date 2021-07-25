""" Contains Duplicate
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
Test with: python -m unittest contains_duplicate.py
"""

import unittest
from typing import List


class Solution:
    class Solution:
        def containsDuplicate(self, nums: List[int]) -> bool:
            pass


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_no_duplicate(self):
        nums = [1, 2, 3, 4]
        answer = self.solution.containsDuplicate(nums)
        self.assertIs(answer, False)

    def test_one_duplicate(self):
        nums = [1, 2, 3, 1]
        answer = self.solution.containsDuplicate(nums)
        self.assertIs(answer, True)

    def test_multiple_duplicates(self):
        nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
        answer = self.solution.containsDuplicate(nums)
        self.assertIs(answer, True)


if __name__ == 'main':
    unittest.main()
