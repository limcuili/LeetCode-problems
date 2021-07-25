""" Best Time to Buy and Sell Stock
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
Test with: python -m unittest best_time_to_buy_and_sell_stock.py
"""

import unittest
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = max(prices) # if you want to remove the complexity required for max(), you could set sys.maxsize
        profit = 0
        for price in prices:
            if price < min_price: min_price = price
            if price - min_price > profit: profit = price - min_price
        return profit


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_no_profit(self):
        prices = [7, 6, 4, 3, 1]
        expected_answer = 0
        answer = self.solution.maxProfit(prices)
        self.assertEqual(expected_answer, answer)

    def test_one_positive_solution(self):
        prices = [7, 6, 4, 3, 11]
        expected_answer = 8
        answer = self.solution.maxProfit(prices)
        self.assertEqual(expected_answer, answer)

    def test_get_higher_profit(self):
        prices = [7, 6, 4, 3, 10, 11]
        expected_answer = 8
        answer = self.solution.maxProfit(prices)
        self.assertEqual(expected_answer, answer)


if __name__ == 'main':
    unittest.main()
