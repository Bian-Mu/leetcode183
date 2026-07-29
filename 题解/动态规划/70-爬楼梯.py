# https://leetcode.cn/problems/climbing-stairs/
# Source: https://walkccc.me/LeetCode/problems/70/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def climbStairs(self, n: int) -> int:
    # dp[i] := the number of ways to climb to the i-th stair
    dp = [1, 1] + [0] * (n - 1)

    for i in range(2, n + 1):
      dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]
