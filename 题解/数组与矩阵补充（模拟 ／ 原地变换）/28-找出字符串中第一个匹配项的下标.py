# https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string/
# Source: https://walkccc.me/LeetCode/problems/28/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def strStr(self, haystack: str, needle: str) -> int:
    m = len(haystack)
    n = len(needle)

    for i in range(m - n + 1):
      if haystack[i:i + n] == needle:
        return i

    return -1
