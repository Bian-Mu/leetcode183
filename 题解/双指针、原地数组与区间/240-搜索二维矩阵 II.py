# https://leetcode.cn/problems/search-a-2d-matrix-ii/
# Source: https://walkccc.me/LeetCode/problems/240/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
    r = 0
    c = len(matrix[0]) - 1

    while r < len(matrix) and c >= 0:
      if matrix[r][c] == target:
        return True
      if target < matrix[r][c]:
        c -= 1
      else:
        r += 1

    return False
