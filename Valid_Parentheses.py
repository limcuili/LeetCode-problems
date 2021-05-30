""" Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
Test with: python -m unittest Valid_Parentheses.py
"""

import unittest


class Solution:
    def isValid(self, s: str) -> bool:
        parentheses_pairs = {")": "(", "}": "{", "]": "["}
        stack = []
        for character in s:
            if character in parentheses_pairs:
                if stack and parentheses_pairs[character] == stack[-1]:
                    top = stack.pop()
                    if parentheses_pairs[character] != top:
                        return False
                else:
                    return False
            else:
                stack.append(character)

        return stack == []


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_single_parentheses(self):
        s = '()'
        answer = self.solution.isValid(s)
        self.assertIs(answer, True)

    def test_consecutive_parentheses(self):
        s = '()[]{}'
        answer = self.solution.isValid(s)
        self.assertIs(answer, True)

    def test_stack_parentheses(self):
        s = '{[]}'
        answer = self.solution.isValid(s)
        self.assertIs(answer, True)

    def test_wrong_parentheses(self):
        s = '(]'
        answer = self.solution.isValid(s)
        self.assertIs(answer, False)

    def test_swapped_position_parentheses(self):
        s = '([)]'
        answer = self.solution.isValid(s)
        self.assertIs(answer, False)

    def test_single_parentheses(self):
        s = ']'
        answer = self.solution.isValid(s)
        self.assertIs(answer, False)
