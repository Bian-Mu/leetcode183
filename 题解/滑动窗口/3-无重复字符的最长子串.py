# https://leetcode.cn/problems/longest-substring-without-repeating-characters/
# Source: https://walkccc.me/LeetCode/problems/3/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    ans = 0
    count = collections.Counter()

    l = 0
    for r, c in enumerate(s):
      count[c] += 1
      while count[c] > 1:
        count[s[l]] -= 1
        l += 1
      ans = max(ans, r - l + 1)

    return ans
