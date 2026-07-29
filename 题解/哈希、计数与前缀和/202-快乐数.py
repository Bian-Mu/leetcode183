# https://leetcode.cn/problems/happy-number/
# Source: https://walkccc.me/LeetCode/problems/202/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def isHappy(self, n: int) -> bool:
    def squaredSum(n: int) -> bool:
      summ = 0
      while n > 0:
        summ += pow(n % 10, 2)
        n //= 10
      return summ

    slow = squaredSum(n)
    fast = squaredSum(squaredSum(n))

    while slow != fast:
      slow = squaredSum(slow)
      fast = squaredSum(squaredSum(fast))

    return slow == 1
