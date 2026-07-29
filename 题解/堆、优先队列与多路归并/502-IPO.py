# https://leetcode.cn/problems/ipo/
# Source algorithm: https://walkccc.me/LeetCode/problems/502/
# SPDX-License-Identifier: MIT
# Python translation of the source algorithm; source copyright (c) 2019-2026 P.-Y. Chen.

import heapq


class Solution:
  def findMaximizedCapital(
      self, k: int, w: int, profits: list[int], capital: list[int]
  ) -> int:
    projects = sorted(zip(capital, profits))
    available: list[int] = []
    i = 0
    for _ in range(k):
      while i < len(projects) and projects[i][0] <= w:
        heapq.heappush(available, -projects[i][1])
        i += 1
      if not available:
        break
      w -= heapq.heappop(available)
    return w
