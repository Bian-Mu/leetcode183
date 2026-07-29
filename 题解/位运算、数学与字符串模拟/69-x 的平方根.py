# https://leetcode.cn/problems/sqrtx/
# Source: https://walkccc.me/LeetCode/problems/69/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def mySqrt(self, x: int) -> int:
    return bisect.bisect_right(range(x + 1), x,
                               key=lambda m: m * m) - 1
