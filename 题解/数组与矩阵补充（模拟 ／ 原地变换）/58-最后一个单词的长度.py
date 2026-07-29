# https://leetcode.cn/problems/length-of-last-word/
# Source: https://walkccc.me/LeetCode/problems/58/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def lengthOfLastWord(self, s: str) -> int:
    i = len(s) - 1

    while i >= 0 and s[i] == ' ':
      i -= 1
    lastIndex = i
    while i >= 0 and s[i] != ' ':
      i -= 1

    return lastIndex - i
