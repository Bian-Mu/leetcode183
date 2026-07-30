# https://leetcode.cn/problems/unique-paths-ii/
# Source: https://walkccc.me/LeetCode/problems/63/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    # dp[i][j] := the number of unique paths from (0, 0) to (i, j)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    dp[0][1] = 1  # Can also set dp[1][0] = 1.

    for i in range(1, m + 1):
      for j in range(1, n + 1):
        if obstacleGrid[i - 1][j - 1] == 0:
          dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[m][n]

  def mysolution(self,obstacleGrid: list[list[int]])-> int:
    m,n=len(obstacleGrid),len(obstacleGrid[0])
    dp=[[0]*n for _ in range(m)]
    dp[0][0]=1
    
    if obstacleGrid[0][0]==1:
      return 0
    
    for i in range(0,m):
      for j in range(0,n):
        if obstacleGrid[i][j]==0 and i+j!=0:
          dp[i][j]=(dp[i][j-1] if j>0 else 0) + (dp[i-1][j] if i>0 else 0)
    
    return dp[m-1][n-1]