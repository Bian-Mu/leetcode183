# https://leetcode.cn/problems/gas-station/
# Source: https://walkccc.me/LeetCode/problems/134/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
    ans = 0
    net = 0
    summ = 0

    # Try to start from each index.
    for i in range(len(gas)):
      net += gas[i] - cost[i]
      summ += gas[i] - cost[i]
      if summ < 0:
        summ = 0
        ans = i + 1  # Start from the next index.

    return -1 if net < 0 else ans
