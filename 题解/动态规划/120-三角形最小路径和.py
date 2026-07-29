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
