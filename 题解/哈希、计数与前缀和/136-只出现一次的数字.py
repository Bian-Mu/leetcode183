# https://leetcode.cn/problems/single-number/
# Source: https://walkccc.me/LeetCode/problems/136/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def singleNumber(self, nums: list[int]) -> int:
    return functools.reduce(operator.xor, nums, 0)

  def mysolution(self, nums: list[int])->int:
    result=nums[0]
    
    for i in range(1,len(nums)):
      result^=nums[i]
    
    return result