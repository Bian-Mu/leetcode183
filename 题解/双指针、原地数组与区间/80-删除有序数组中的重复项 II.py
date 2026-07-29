# https://leetcode.cn/problems/remove-duplicates-from-sorted-array-ii/
# Source: https://walkccc.me/LeetCode/problems/80/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def removeDuplicates(self, nums: list[int]) -> int:
    i = 0

    for num in nums:
      if i < 2 or num != nums[i - 2]:
        nums[i] = num
        i += 1

    return i
