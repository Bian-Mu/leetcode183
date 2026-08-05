# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iii/
# Source: https://walkccc.me/LeetCode/problems/123/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)
import math

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

  def mysolution(self, prices: list[int])->int:
    times=3
    
    buy=[-math.inf for _ in range(times)]
    sell=[0 for _ in range(times)]
    
    for price in prices:
      for i in range(1,times):
        buy[i]=max(buy[i],sell[i-1]-price)
        sell[i]=max(sell[i],buy[i]+price)
    
    return sell[times-1]