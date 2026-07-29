# https://leetcode.cn/problems/add-binary/
# Source: https://walkccc.me/LeetCode/problems/67/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def addBinary(self, a: str, b: str) -> str:
    ans = []
    carry = 0
    i = len(a) - 1
    j = len(b) - 1

    while i >= 0 or j >= 0 or carry:
      if i >= 0:
        carry += int(a[i])
        i -= 1
      if j >= 0:
        carry += int(b[j])
        j -= 1
      ans.append(str(carry % 2))
      carry //= 2

    return ''.join(reversed(ans))
