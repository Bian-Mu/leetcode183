# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iii/
# Source: https://walkccc.me/LeetCode/problems/123/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def maxProfit(self, prices: list[int]) -> int:
    sellTwo = 0
    holdTwo = -math.inf
    sellOne = 0
    holdOne = -math.inf

    for price in prices:
      sellTwo = max(sellTwo, holdTwo + price)
      holdTwo = max(holdTwo, sellOne - price)
      sellOne = max(sellOne, holdOne + price)
      holdOne = max(holdOne, -price)

    return sellTwo
