# https://leetcode.cn/problems/minimum-size-subarray-sum/
# Source: https://walkccc.me/LeetCode/problems/209/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def minSubArrayLen(self, target: int, nums: list[int]) -> int:
    ans = math.inf
    summ = 0
    j = 0

    for i, num in enumerate(nums):
      summ += num
      while summ >= target:
        ans = min(ans, i - j + 1)
        summ -= nums[j]
        j += 1

    return 0 if ans == math.inf else ans
