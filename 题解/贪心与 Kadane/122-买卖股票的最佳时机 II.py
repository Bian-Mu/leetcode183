# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/
# Source: https://walkccc.me/LeetCode/problems/122/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def maxProfit(self, prices: list[int]) -> int:
    sell = 0
    hold = -math.inf

    for price in prices:
      sell = max(sell, hold + price)
      hold = max(hold, sell - price)

    return sell
