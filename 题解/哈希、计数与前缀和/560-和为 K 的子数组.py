# https://leetcode.cn/problems/subarray-sum-equals-k/
# Source: https://walkccc.me/LeetCode/problems/560/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def subarraySum(self, nums: list[int], k: int) -> int:
    ans = 0
    prefix = 0
    count = collections.Counter({0: 1})

    for num in nums:
      prefix += num
      ans += count[prefix - k]
      count[prefix] += 1

    return ans
