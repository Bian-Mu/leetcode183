# https://leetcode.cn/problems/reverse-words-in-a-string/
# Source: https://walkccc.me/LeetCode/problems/151/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def reverseWords(self, s: str) -> str:
    return ' '.join(reversed(s.split()))
