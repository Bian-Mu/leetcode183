# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iv/
# Source: https://walkccc.me/LeetCode/problems/188/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def maxProfit(self, k: int, prices: list[int]) -> int:
    if k >= len(prices) // 2:
      sell = 0
      hold = -math.inf

      for price in prices:
        sell = max(sell, hold + price)
        hold = max(hold, sell - price)

      return sell

    sell = [0] * (k + 1)
    hold = [-math.inf] * (k + 1)

    for price in prices:
      for i in range(k, 0, -1):
        sell[i] = max(sell[i], hold[i] + price)
        hold[i] = max(hold[i], sell[i - 1] - price)

    return sell[k]

  def mysolution(self, k:int, prices: list[int])->int:
    buy=[-float('inf') for _ in range(k+1)]
    sell=[0 for _ in range(k+1)]
    
    for price in prices:
      for i in range(1,k+1):
        buy[i]=max(buy[i],sell[i-1]-price)
        sell[i]=max(sell[i],buy[i]+price)
    
    return sell[k]