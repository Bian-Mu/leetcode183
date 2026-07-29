# https://leetcode.cn/problems/roman-to-integer/
# Source: https://walkccc.me/LeetCode/problems/13/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def romanToInt(self, s: str) -> int:
    ans = 0
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
             'C': 100, 'D': 500, 'M': 1000}

    for a, b in zip(s, s[1:]):
      if roman[a] < roman[b]:
        ans -= roman[a]
      else:
        ans += roman[a]

    return ans + roman[s[-1]]
