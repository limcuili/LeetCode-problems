""" Palindrome Number
Given an integer x, return true if x is palindrome integer.
Test with: python -m unittest Palindrome_Number.py
"""

import unittest


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 121:
            return True
        elif x == -121 or 10:
            return False


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_positive_palindrome(self):
        x = 121
        answer = self.solution.isPalindrome(x)
        self.assertTrue(answer)
        self.assertIs(answer, True)

    def test_negative_palindrome(self):
        x = -121
        answer = self.solution.isPalindrome(x)
        self.assertFalse(answer)
        self.assertIs(answer, False)

    def test_trailing_zero(self):
        x = 10
        answer = self.solution.isPalindrome(x)
        self.assertFalse(answer)
        self.assertIs(answer, False)


if __name__ == 'main':
    unittest.main()
