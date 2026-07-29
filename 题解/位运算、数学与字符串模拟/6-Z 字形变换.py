# https://leetcode.cn/problems/zigzag-conversion/
# Source: https://walkccc.me/LeetCode/problems/6/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def convert(self, s: str, numRows: int) -> str:
    rows = [''] * numRows
    k = 0
    direction = (numRows == 1) - 1

    for c in s:
      rows[k] += c
      if k == 0 or k == numRows - 1:
        direction *= -1
      k += direction

    return ''.join(rows)
