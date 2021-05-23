""" Two Sums
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
Test with: python -m unittest Two_Sums.py
"""

import unittest

class Solution:
    def two_sum_1(self, nums: list[int], target: int) -> list[int]:
        for i, numi in enumerate(nums):
            for j, numj in enumerate(nums):
                if numi + numj == target and i != j:
                    return [i, j]

    def two_sum_2(self, nums: list[int], target: int) -> list[int]:
        done = {}
        for i, num in enumerate(nums):
            remainder = target - num
            if remainder not in done:
                done[num] = i
            else:
                return [done[remainder], i]

    def twoSum(self, nums: list[int], target:int) -> list[int]:
        return self.two_sum_1(nums, target)


class Solution2:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        done = {}
        for i, num in enumerate(nums):
            remainder = target - num
            if remainder not in done:
                done[num] = i
            else:
                return [done[remainder], i]

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution2()

    def test_returns_two_indices_as_list(self):
        nums = [2, 7, 11, 15]
        target = 9
        expected_answer = [0, 1]
        answer = self.solution.twoSum(nums, target)
        self.assertEqual(expected_answer, answer)

    def test_returns_two_indices_as_list_2(self):
        nums = [3, 2, 4]
        target = 6
        expected_answer = [1, 2]
        answer = self.solution.twoSum(nums, target)
        self.assertEqual(expected_answer, answer)

if __name__ == 'main':
    unittest.main()