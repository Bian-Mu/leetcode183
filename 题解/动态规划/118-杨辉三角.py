# https://leetcode.cn/problems/pascals-triangle/
# Source: https://walkccc.me/LeetCode/problems/118/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def generate(self, numRows: int) -> list[list[int]]:
    ans = []

    for i in range(numRows):
      ans.append([1] * (i + 1))

    for i in range(2, numRows):
      for j in range(1, len(ans[i]) - 1):
        ans[i][j] = ans[i - 1][j - 1] + ans[i - 1][j]

    return ans

  def mysolution(self, numRows:int) -> list[list[int]]:
    dp=[]
    
    for i in range(numRows):
      dp.append(([1] * (i+1)))
    
    for i in range(2,numRows):
      for j in range(1,i):
        dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
    
    return dp