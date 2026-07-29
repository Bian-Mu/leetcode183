# https://leetcode.cn/problems/maximum-subarray/
# Source: https://walkccc.me/LeetCode/problems/53/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def maxSubArray(self, nums: list[int]) -> int:
    # dp[i] := the maximum sum subarray ending in i
    dp = [0] * len(nums)

    dp[0] = nums[0]
    for i in range(1, len(nums)):
      dp[i] = max(nums[i], dp[i - 1] + nums[i])

    return max(dp)
