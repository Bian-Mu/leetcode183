# https://leetcode.cn/problems/find-peak-element/
# Source: https://walkccc.me/LeetCode/problems/162/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def findPeakElement(self, nums: list[int]) -> int:
    l = 0
    r = len(nums) - 1

    while l < r:
      m = (l + r) // 2
      if nums[m] >= nums[m + 1]:
        r = m
      else:
        l = m + 1

    return l
