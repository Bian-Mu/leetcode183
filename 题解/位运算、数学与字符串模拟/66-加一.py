# https://leetcode.cn/problems/plus-one/
# Source: https://walkccc.me/LeetCode/problems/66/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def plusOne(self, digits: list[int]) -> list[int]:
    for i, d in reversed(list(enumerate(digits))):
      if d < 9:
        digits[i] += 1
        return digits
      digits[i] = 0

    return [1] + digits
