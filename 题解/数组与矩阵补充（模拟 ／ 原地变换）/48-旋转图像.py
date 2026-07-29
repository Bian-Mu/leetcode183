# https://leetcode.cn/problems/rotate-image/
# Source: https://walkccc.me/LeetCode/problems/48/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def rotate(self, matrix: list[list[int]]) -> None:
    matrix.reverse()
    for i, j in itertools.combinations(range(len(matrix)), 2):
      matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
