""" Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without repeating characters.
Test with: python -m unittest Longest_Substring_Without_Repeating_Characters.py
"""

import unittest


class Solution:
    def lengthOfLongestSubstring1(self, s: str) -> int:
        max_length = 0
        starting_position = 0
        characters_seen = {}

        for index, character in enumerate(s):
            if character in characters_seen and characters_seen[character] >= starting_position:
                starting_position = characters_seen[character] + 1
            else:
                max_length = max(max_length, index-starting_position+1)
            characters_seen[character] = index

        return max_length

    def lengthOfLongestSubstring2(self, s: str) -> int:
        # TODO: if you want an overly complicated solution, implement a suffix tree.
        return None

    def lengthOfLongestSubstring(self, s: str) -> int:
        # hook in whichever of the above implementation you want.
        return self.lengthOfLongestSubstring1(s)


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_front_substring(self):
        s = 'abcbb'
        expected_answer = 3
        answer = self.solution.lengthOfLongestSubstring(s)
        self.assertEqual(expected_answer, answer)

    def test_back_substring(self):
        s = 'abcabcd'
        expected_answer = 4
        answer = self.solution.lengthOfLongestSubstring(s)
        self.assertEqual(expected_answer, answer)

    def test_single_substring(self):
        s = 'bbbbbb'
        expected_answer = 1
        answer = self.solution.lengthOfLongestSubstring(s)
        self.assertEqual(expected_answer, answer)

    def test_empty_string(self):
        s = ''
        expected_answer = 0
        answer = self.solution.lengthOfLongestSubstring(s)
        self.assertEqual(expected_answer, answer)

    def test_not_subsequence(self):
        s = 'pwwkew'
        expected_answer = 3
        answer = self.solution.lengthOfLongestSubstring(s)
        self.assertEqual(expected_answer, answer)


if __name__ == 'main':
    unittest.main()
