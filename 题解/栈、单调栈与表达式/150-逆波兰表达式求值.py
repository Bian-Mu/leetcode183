# https://leetcode.cn/problems/evaluate-reverse-polish-notation/
# Source: https://walkccc.me/LeetCode/problems/150/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def evalRPN(self, tokens: list[str]) -> int:
    stack = []
    op = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: int(a / b),
    }

    for token in tokens:
      if token in op:
        b = stack.pop()
        a = stack.pop()
        stack.append(op[token](a, b))
      else:
        stack.append(int(token))

    return stack.pop()
