# https://leetcode.cn/problems/is-subsequence/
# Source: https://walkccc.me/LeetCode/problems/392/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def isSubsequence(self, s: str, t: str) -> bool:
    if not s:
      return True

    i = 0
    for c in t:
      if s[i] == c:
        i += 1
        if i == len(s):
          return True

    return False
