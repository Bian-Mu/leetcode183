# https://leetcode.cn/problems/coin-change/
# Source: https://walkccc.me/LeetCode/problems/322/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def coinChange(self, coins: list[int], amount: int) -> int:
    # dp[i] := the minimum number Of coins to make up i
    dp = [0] + [amount + 1] * amount

    for coin in coins:
      for i in range(coin, amount + 1):
        dp[i] = min(dp[i], dp[i - coin] + 1)

    return -1 if dp[amount] == amount + 1 else dp[amount]

  def mysolution(self, coins:list[int], amount:int)->int:
    dp=[float('inf')]*(amount+1)
    dp[0]=0
    
    for coin in coins:
      for num in range(coin,amount+1):
        dp[num]=min(dp[num],dp[num-coin]+1)
        
    return -1 if dp[amount]==float('inf') else dp[amount]