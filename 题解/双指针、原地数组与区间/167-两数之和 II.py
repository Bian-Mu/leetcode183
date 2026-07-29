# https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/
# Source: https://walkccc.me/LeetCode/problems/167/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def twoSum(self, numbers: list[int], target: int) -> list[int]:
    l = 0
    r = len(numbers) - 1

    while l < r:
      summ = numbers[l] + numbers[r]
      if summ == target:
        return [l + 1, r + 1]
      if summ < target:
        l += 1
      else:
        r -= 1
