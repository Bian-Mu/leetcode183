# https://leetcode.cn/problems/partition-labels/
# Source: https://walkccc.me/LeetCode/problems/763/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def partitionLabels(self, s: str) -> list[int]:
    ans = []
    letterToRightmostIndex = {c: i for i, c in enumerate(s)}

    l = 0  # the leftmost index of the current running string
    r = 0  # the rightmost index of the current running string

    for i, c in enumerate(s):
      r = max(r, letterToRightmostIndex[c])
      if i == r:
        ans.append(r - l + 1)
        l = r + 1

    return ans
