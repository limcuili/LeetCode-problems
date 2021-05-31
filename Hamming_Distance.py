""" Hamming Distance
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Test with: python -m unittest Hamming_Distance.py
"""

import unittest


class Solution:
    def hammingDistance1(self, x: int, y: int) -> int:
        binary_x = "{:032b}".format(x)
        binary_y = "{:032b}".format(y)
        differences = [i for i, j in zip(binary_x, binary_y) if i != j]
        return len(differences)

    def hammingDistance2(self, x: int, y: int) -> int:
        # TODO: implement with bitwise operations.
        return None

    def hammingDistance(self, x: int, y: int) -> int:
        # hook in whichever of the above implementation you want.
        return self.hammingDistance1(x, y)


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

    def test_edge_case(self):
        x = 4
        y = 14
        expected_answer = 2
        answer = self.solution.hammingDistance(x, y)
        self.assertEqual(expected_answer, answer)
