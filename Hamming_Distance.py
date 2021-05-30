""" Hamming Distance
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Test with: python -m unittest Hamming_Distance.py
"""

import unittest


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return None


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_one_difference(self):
        x = 3
        y = 1
        expected_answer = 1
        answer = self.solution.hammingDistance(x, y)
        self.assertEqual(expected_answer, answer)

    def test_two_difference(self):
        x = 4
        y = 1
        expected_answer = 2
        answer = self.solution.hammingDistance(x, y)
        self.assertEqual(expected_answer, answer)
