# https://leetcode.cn/problems/basic-calculator/
# Source: https://walkccc.me/LeetCode/problems/224/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def calculate(self, s: str) -> int:
    ans = 0
    num = 0
    sign = 1
    stack = [sign]  # stack[-1]: the current environment's sign

    for c in s:
      if c.isdigit():
        num = num * 10 + int(c)
      elif c == '(':
        stack.append(sign)
      elif c == ')':
        stack.pop()
      elif c == '+' or c == '-':
        ans += sign * num
        sign = (1 if c == '+' else -1) * stack[-1]
        num = 0

    return ans + sign * num

  def mysolution(self, s:str)->int:
    sign=1
    num=0
    ans=0
    stack=[sign]
    
    for ch in s:
      if ch.isdigit():
        num=num*10+int(ch)
      elif ch=='(':
        stack.append(sign)
      elif ch==')':
        stack.pop()
      elif ch=='+' or ch=='-':
        ans+=sign*num
        if ch=='+':
          sign=1*stack[-1]
        else:
          sign=(-1)*stack[-1]
        num=0
        
    return ans+num*sign