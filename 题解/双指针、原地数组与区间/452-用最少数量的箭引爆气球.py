# https://leetcode.cn/problems/minimum-number-of-arrows-to-burst-balloons/
# Source: https://walkccc.me/LeetCode/problems/452/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def findMinArrowShots(self, points: list[list[int]]) -> int:
    ans = 0
    arrowX = -math.inf

    for point in sorted(points, key=lambda x: x[1]):
      if point[0] > arrowX:
        ans += 1
        arrowX = point[1]

    return ans
