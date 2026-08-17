# https://leetcode.cn/problems/jump-game/
# Source: https://walkccc.me/LeetCode/problems/55/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def canJump(self, nums: list[int]) -> bool:
    i = 0
    reach = 0

    while i < len(nums) and i <= reach:
      reach = max(reach, i + nums[i])
      i += 1

    return i == len(nums)

  def mysolution(self, nums: list[int])->bool:
    if len(nums)==1:
      return True
    
    currMax=0+nums[0]
    
    for i,val in enumerate(nums[1:],start=1):
      if i>currMax:
        return False
      
      if currMax>=len(nums)-1:
        return True
      
      currMax=max(currMax,i+val)
    
    return False