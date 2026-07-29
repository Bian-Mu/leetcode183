# https://leetcode.cn/problems/perfect-squares/
# Source: https://walkccc.me/LeetCode/problems/279/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

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
