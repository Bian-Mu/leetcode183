# https://leetcode.cn/problems/trapping-rain-water/
# Source: https://walkccc.me/LeetCode/problems/42/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def trap(self, height: list[int]) -> int:
    n = len(height)
    l = [0] * n  # l[i] := max(height[0..i])
    r = [0] * n  # r[i] := max(height[i..n))

    for i, h in enumerate(height):
      l[i] = h if i == 0 else max(h, l[i - 1])

    for i, h in reversed(list(enumerate(height))):
      r[i] = h if i == n - 1 else max(h, r[i + 1])

    return sum(min(l[i], r[i]) - h
               for i, h in enumerate(height))

  def mysolution(self, height: list[int])->int:
    l=[0]*len(height)
    r=[0]*len(height)
    sum=0
    
    for i in range(len(height)):
      if i==0:
        l[i]=height[i]
      else:
        l[i]=max(l[i-1],height[i])
        
    for j in range(len(height)-1,-1,-1):
      if j==len(height)-1:
        r[j]=height[j]
      else:
        r[j]=max(r[j+1],height[j])
    
    for k in range(len(height)):
      sum+=min(l[k],r[k])-height[k]
    
    return sum