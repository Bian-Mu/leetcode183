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
