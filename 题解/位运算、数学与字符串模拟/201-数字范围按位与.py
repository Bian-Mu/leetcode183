# https://leetcode.cn/problems/bitwise-and-of-numbers-range/
# Source: https://walkccc.me/LeetCode/problems/201/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def rangeBitwiseAnd(self, m: int, n: int) -> int:
    return self.rangeBitwiseAnd(m >> 1, n >> 1) << 1 if m < n else m
