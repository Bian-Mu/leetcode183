# https://leetcode.cn/problems/kth-largest-element-in-an-array/
# Source: https://walkccc.me/LeetCode/problems/215/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def findKthLargest(self, nums: list[int], k: int) -> int:
    minHeap = []

    for num in nums:
      heapq.heappush(minHeap, num)
      if len(minHeap) > k:
        heapq.heappop(minHeap)

    return minHeap[0]
