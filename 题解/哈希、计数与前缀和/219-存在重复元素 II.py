# https://leetcode.cn/problems/contains-duplicate-ii/
# Source: https://walkccc.me/LeetCode/problems/219/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
    seen = set()

    for i, num in enumerate(nums):
      if i > k:
        seen.remove(nums[i - k - 1])
      if num in seen:
        return True
      seen.add(num)

    return False
