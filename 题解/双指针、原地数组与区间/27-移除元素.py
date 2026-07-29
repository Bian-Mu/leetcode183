# https://leetcode.cn/problems/remove-element/
# Source: https://walkccc.me/LeetCode/problems/27/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def removeElement(self, nums: list[int], val: int) -> int:
    i = 0

    for num in nums:
      if num != val:
        nums[i] = num
        i += 1

    return i
