# https://leetcode.cn/problems/min-stack/
# Source: https://walkccc.me/LeetCode/problems/155/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class MinStack:
  def __init__(self):
    self.stack = []

  def push(self, x: int) -> None:
    mn = x if not self.stack else min(self.stack[-1][1], x)
    self.stack.append([x, mn])

  def pop(self) -> None:
    self.stack.pop()

  def top(self) -> int:
    return self.stack[-1][0]

  def getMin(self) -> int:
    return self.stack[-1][1]

class MySolution:
  def __init__(self) -> None:
    self.stack=[]
    self.mins=[]
  
  def push(self,val):
    self.stack.append(val)
    if self.mins:
      self.mins.append(min(self.mins[-1],val))
    else:
      self.mins.append(val)
  
  def pop(self)->int:
    if self.stack:
      self.mins.pop()
      return self.stack.pop()
    else:
      return -1
  
  def top(self)->int:
    return self.stack[-1]
  
  def getMin(self)-> int:
    return self.mins[-1]