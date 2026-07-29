# https://leetcode.cn/problems/valid-palindrome/
# Source: https://walkccc.me/LeetCode/problems/125/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def isPalindrome(self, s: str) -> bool:
    l = 0
    r = len(s) - 1

    while l < r:
      while l < r and not s[l].isalnum():
        l += 1
      while l < r and not s[r].isalnum():
        r -= 1
      if s[l].lower() != s[r].lower():
        return False
      l += 1
      r -= 1

    return True
