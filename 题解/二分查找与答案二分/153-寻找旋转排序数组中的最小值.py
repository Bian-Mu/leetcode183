# https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/
# Source: https://walkccc.me/LeetCode/problems/153/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def findMin(self, nums: list[int]) -> int:
    l = 0
    r = len(nums) - 1

    while l < r:
      m = (l + r) // 2
      if nums[m] < nums[r]:
        r = m
      else:
        l = m + 1

    return nums[l]
