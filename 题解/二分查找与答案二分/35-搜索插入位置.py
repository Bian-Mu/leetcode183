# https://leetcode.cn/problems/search-insert-position/
# Source: https://walkccc.me/LeetCode/problems/35/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def searchInsert(self, nums: list[int], target: int) -> int:
    l = 0
    r = len(nums)

    while l < r:
      m = (l + r) // 2
      if nums[m] == target:
        return m
      if nums[m] < target:
        l = m + 1
      else:
        r = m

    return l

  def mysolution(self, nums: list[int], target:int)->int:
    left,right=0,len(nums)
    # 插入到末尾
    
    while left<right:
      mid=(left+right)//2
      
      if nums[mid]==target:
        return mid
      elif nums[mid]>target:
        right=mid
      else:
        left=mid+1
    
    return left