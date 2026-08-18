# https://leetcode.cn/problems/largest-rectangle-in-histogram/
# Source: https://walkccc.me/LeetCode/problems/84/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def largestRectangleArea(self, heights: list[int]) -> int:
    ans = 0
    stack = []

    for i in range(len(heights) + 1):
      while stack and (i == len(heights) or heights[stack[-1]] > heights[i]):
        h = heights[stack.pop()]
        w = i - stack[-1] - 1 if stack else i
        ans = max(ans, h * w)
      stack.append(i)

    return ans

  def mysolution(self, heights: list[int])->int:
    stack=[]
    ans=0
    heights=heights+[0]
    for i,height in enumerate(heights):
      while stack and height<heights[stack[-1]]:
        h=heights[stack.pop()]
        w=i-stack[-1]-1 if stack else i-0
        ans=max(ans,w*h)
      stack.append(i)
    return ans