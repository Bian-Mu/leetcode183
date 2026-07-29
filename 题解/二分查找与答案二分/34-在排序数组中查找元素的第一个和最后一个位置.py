# https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/
# Source: https://walkccc.me/LeetCode/problems/34/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def searchRange(self, nums: list[int], target: int) -> list[int]:
    l = bisect_left(nums, target)
    if l == len(nums) or nums[l] != target:
      return -1, -1
    r = bisect_right(nums, target) - 1
    return l, r
