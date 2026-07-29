# https://leetcode.cn/problems/reverse-bits/
# Source: https://walkccc.me/LeetCode/problems/190/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def reverseBits(self, n: int) -> int:
    ans = 0

    for i in range(32):
      if n >> i & 1:
        ans |= 1 << 31 - i

    return ans
