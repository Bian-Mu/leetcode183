# https://leetcode.cn/problems/h-index/
# Source: https://walkccc.me/LeetCode/problems/274/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def hIndex(self, citations: list[int]) -> int:
    n = len(citations)
    accumulate = 0
    count = [0] * (n + 1)

    for citation in citations:
      count[min(citation, n)] += 1

    # To find the maximum h-index, loop from the back to the front.
    # i := the candidate's h-index
    for i, c in reversed(list(enumerate(count))):
      accumulate += c
      if accumulate >= i:
        return i
