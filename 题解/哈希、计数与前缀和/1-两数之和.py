# https://leetcode.cn/problems/two-sum/
# Source: https://walkccc.me/LeetCode/problems/1/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def twoSum(self, nums: list[int], target: int) -> list[int]:
    numToIndex = {}

    for i, num in enumerate(nums):
      if target - num in numToIndex:
        return numToIndex[target - num], i
      numToIndex[num] = i
