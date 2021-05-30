""" Palindrome Number
Given an integer x, return true if x is palindrome integer.
Test with: python -m unittest Palindrome_Number.py
"""

import unittest


class Solution:
    def isPalindrome1(self, x: int) -> bool:
        reversed_string = str(x)[::-1]
        return str(x) == reversed_string

    def isPalindrome2(self, x: int) -> bool:
        left_pointer = 0
        right_pointer = len(str(x)) - 1
        while left_pointer < right_pointer:
            if str(x)[left_pointer] != str(x)[right_pointer]:
                return False
            else:
                left_pointer += 1
                right_pointer -= 1
        return True

    def isPalindrome(self, x: int) -> bool:
        # hook in whichever of the above implementation you want.
        return self.isPalindrome2(x)


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
