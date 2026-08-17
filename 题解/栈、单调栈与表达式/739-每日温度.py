# https://leetcode.cn/problems/daily-temperatures/
# Source: https://walkccc.me/LeetCode/problems/739/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
    ans = [0] * len(temperatures)
    stack = []  # a decreasing stack

    for i, temperature in enumerate(temperatures):
      while stack and temperature > temperatures[stack[-1]]:
        index = stack.pop()
        ans[index] = i - index
      stack.append(i)

    return ans

  def mysolution(self, temperatures: list[int])->list[int]:
    ans=[0]*len(temperatures)
    stack=[]
    
    for i,temper in enumerate(temperatures):
      while stack and temper>temperatures[stack[-1]]:
        index=stack.pop()
        ans[index]=i-index
      stack.append(i)
    
    return ans