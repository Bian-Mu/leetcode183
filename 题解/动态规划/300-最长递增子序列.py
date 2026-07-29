# https://leetcode.cn/problems/longest-increasing-subsequence/
# Source: https://walkccc.me/LeetCode/problems/300/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def lengthOfLIS(self, nums: list[int]) -> int:
    if not nums:
      return 0

    # dp[i] := the length of LIS ending in nums[i]
    dp = [1] * len(nums)

    for i in range(1, len(nums)):
      for j in range(i):
        if nums[j] < nums[i]:
          dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)
