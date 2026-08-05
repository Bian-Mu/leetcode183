# https://leetcode.cn/problems/triangle/
# Source: https://walkccc.me/LeetCode/problems/120/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def minimumTotal(self, triangle: list[list[int]]) -> int:
    for i in range(len(triangle) - 2, -1, -1):
      for j in range(i + 1):
        triangle[i][j] += min(triangle[i + 1][j],
                              triangle[i + 1][j + 1])

    return triangle[0][0]

  def mysolution(self, triangle: list[list[int]])->int:
    n = len(triangle)
    
    if not n:
      return 0
    
    dp=[[float('inf')]*(i+1) for i in range(n)]
    dp[0][0]=triangle[0][0]
    
    for i in range(1,n):
      for j in range(i+1):
        if j==0:
          dp[i][j]=dp[i-1][j]+triangle[i][j]
        elif j==i:
          dp[i][j]=dp[i-1][j-1]+triangle[i][j]
        else:
          dp[i][j]=min(dp[i-1][j-1],dp[i-1][j])+triangle[i][j]
          
    return min((dp[n-1]))