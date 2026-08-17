# https://leetcode.cn/problems/powx-n/
# Source: https://walkccc.me/LeetCode/problems/50/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def myPow(self, x: float, n: int) -> float:
    if n == 0:
      return 1
    if n < 0:
      return 1 / self.myPow(x, -n)
    if n % 2 == 1:
      return x * self.myPow(x, n - 1)
    return self.myPow(x * x, n // 2)

  def mysolution(self, x: float, n:int)-> float:
    if not n:
      return 1
    if n==1:
      return x
    if n<0:
      return 1/self.mysolution(x,-n)
    if n%2:
      return x*self.mysolution(x,n-1)
    return self.mysolution(x*x,n//2)