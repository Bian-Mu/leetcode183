# https://leetcode.cn/problems/isomorphic-strings/
# Source: https://walkccc.me/LeetCode/problems/205/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def isIsomorphic(self, s: str, t: str) -> bool:
    return [*map(s.index, s)] == [*map(t.index, t)]
