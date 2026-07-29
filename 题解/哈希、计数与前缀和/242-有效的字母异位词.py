# https://leetcode.cn/problems/valid-anagram/
# Source: https://walkccc.me/LeetCode/problems/242/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
      return False

    count = collections.Counter(s)
    count.subtract(collections.Counter(t))
    return all(freq == 0 for freq in count.values())
