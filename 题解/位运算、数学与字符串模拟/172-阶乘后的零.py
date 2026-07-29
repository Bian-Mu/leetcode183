# https://leetcode.cn/problems/factorial-trailing-zeroes/
# Source: https://walkccc.me/LeetCode/problems/172/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def trailingZeroes(self, n: int) -> int:
    return 0 if n == 0 else n // 5 + self.trailingZeroes(n // 5)
