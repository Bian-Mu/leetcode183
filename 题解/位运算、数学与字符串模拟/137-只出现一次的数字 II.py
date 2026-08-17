# https://leetcode.cn/problems/single-number-ii/
# Source: https://walkccc.me/LeetCode/problems/137/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def singleNumber(self, nums: list[int]) -> int:
    ones = 0
    twos = 0

    for num in nums:
      ones ^= num & ~twos
      twos ^= num & ~ones

    return ones

  def mysolution(self, nums: list[int])->int:
    ans=0
    
    for i in range(32):
      bit=0
      
      for num in nums:
        bit+=(num>>i)&1
      
      if bit%3:
        ans+=1<<bit
    
    return ans