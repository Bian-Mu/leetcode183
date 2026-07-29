# https://leetcode.cn/problems/find-all-anagrams-in-a-string/
# Source: https://walkccc.me/LeetCode/problems/438/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def findAnagrams(self, s: str, p: str) -> list[int]:
    ans = []
    count = collections.Counter(p)
    required = len(p)

    for r, c in enumerate(s):
      count[c] -= 1
      if count[c] >= 0:
        required -= 1
      if r >= len(p):
        count[s[r - len(p)]] += 1
        if count[s[r - len(p)]] > 0:
          required += 1
      if required == 0:
        ans.append(r - len(p) + 1)

    return ans
