# https://leetcode.cn/problems/perfect-squares/
# Source: https://walkccc.me/LeetCode/problems/279/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

import math

class Solution:
  def numSquares(self, n: int) -> int:
    dp = [n] * (n + 1)  # 1^2 x n
    dp[0] = 0  # no way
    dp[1] = 1  # 1^2

    for i in range(2, n + 1):
      j = 1
      while j * j <= i:
        dp[i] = min(dp[i], dp[i - j * j] + 1)
        j += 1

    return dp[n]

  def mysolution(self, n:int)->int:
    Set=set([x*x for x in range(1,math.floor(math.sqrt(n))+1)])
    dp=[x for x in range(n+1)]
    
    for num in Set:
      for i in range(num,n+1):
        dp[i]=min(dp[i],dp[i-num]+1)
    
    return dp[n]