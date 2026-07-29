# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/
# Source: https://walkccc.me/LeetCode/problems/121/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def maxProfit(self, prices: list[int]) -> int:
    sellOne = 0
    holdOne = -math.inf

    for price in prices:
      sellOne = max(sellOne, holdOne + price)
      holdOne = max(holdOne, -price)

    return sellOne
