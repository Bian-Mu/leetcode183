# https://leetcode.cn/problems/unique-paths/
# Source: https://walkccc.me/LeetCode/problems/62/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def uniquePaths(self, m: int, n: int) -> int:
    # dp[i][j] := the number of unique paths from (0, 0) to (i, j)
    dp = [[1] * n for _ in range(m)]

    for i in range(1, m):
      for j in range(1, n):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[-1][-1]

  def mysolution(self, m: int, n: int)-> int:
    val=[[1] for _ in range(n) for _ in range(m)]
    
    for i in range(1,m):
      for j in range(1,n):
        val[i][j]=val[i-1][j]+val[i][j-1]
    
    return val[m-1][n-1]