# https://leetcode.cn/problems/summary-ranges/
# Source: https://walkccc.me/LeetCode/problems/228/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def summaryRanges(self, nums: list[int]) -> list[str]:
    ans = []

    i = 0
    while i < len(nums):
      begin = nums[i]
      while i < len(nums) - 1 and nums[i] == nums[i + 1] - 1:
        i += 1
      end = nums[i]
      if begin == end:
        ans.append(str(begin))
      else:
        ans.append(str(begin) + "->" + str(end))
      i += 1

    return ans
