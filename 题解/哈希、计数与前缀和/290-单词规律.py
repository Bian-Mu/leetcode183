# https://leetcode.cn/problems/word-pattern/
# Source: https://walkccc.me/LeetCode/problems/290/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def wordPattern(self, pattern: str, str: str) -> bool:
    t = str.split()
    return [*map(pattern.index, pattern)] == [*map(t.index, t)]
