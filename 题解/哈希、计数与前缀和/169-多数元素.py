# https://leetcode.cn/problems/majority-element/
# Source: https://walkccc.me/LeetCode/problems/169/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def majorityElement(self, nums: list[int]) -> int:
    ans = None
    count = 0

    for num in nums:
      if count == 0:
        ans = num
      count += (1 if num == ans else -1)

    return ans

  def mysolution(self, nums: list[int])->int:
    result=0
    cnt=0
    
    for num in nums:
      if not cnt:
        result=num
        cnt=1
      elif num==result:
        cnt+=1
      else:
        cnt-=1
    return result