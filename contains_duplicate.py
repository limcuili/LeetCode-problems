""" Contains Duplicate
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
Test with: python -m unittest contains_duplicate.py
"""

import unittest
from typing import List


class Solution:
    def containsDuplicate1(self, nums: List[int]) -> bool:
        # Quadratic time solution
        duplicates_seen = [x for i, x in enumerate(nums) if x in nums[:i]]
        return bool(duplicates_seen)

    def containsDuplicate2(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

    def containsDuplicate(self, nums: List[int]) -> bool:
        # hook in whichever function you want.
        return self.containsDuplicate2(nums)


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
