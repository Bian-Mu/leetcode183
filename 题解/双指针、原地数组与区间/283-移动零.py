# https://leetcode.cn/problems/move-zeroes/
# Source: https://walkccc.me/LeetCode/problems/283/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def moveZeroes(self, nums: list[int]) -> None:
    j = 0
    for num in nums:
      if num != 0:
        nums[j] = num
        j += 1

    for i in range(j, len(nums)):
      nums[i] = 0
