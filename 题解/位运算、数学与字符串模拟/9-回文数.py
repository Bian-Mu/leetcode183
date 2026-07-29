# https://leetcode.cn/problems/palindrome-number/
# Source: https://walkccc.me/LeetCode/problems/9/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def isPalindrome(self, x: int) -> bool:
    if x < 0:
      return False

    rev = 0
    y = x

    while y:
      rev = rev * 10 + y % 10
      y //= 10

    return rev == x
