# https://leetcode.cn/problems/longest-consecutive-sequence/
# Source: https://walkccc.me/LeetCode/problems/128/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def longestConsecutive(self, nums: list[int]) -> int:
    ans = 0
    seen = set(nums)

    for num in seen:
      # `num` is the start of a sequence.
      if num - 1 in seen:
        continue
      length = 0
      while num in seen:
        num += 1
        length += 1
      ans = max(ans, length)

    return ans
