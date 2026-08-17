# https://leetcode.cn/problems/valid-parentheses/
# Source: https://walkccc.me/LeetCode/problems/20/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def isValid(self, s: str) -> bool:
    stack = []

    for c in s:
      if c == '(':
        stack.append(')')
      elif c == '{':
        stack.append('}')
      elif c == '[':
        stack.append(']')
      elif not stack or stack.pop() != c:
        return False

    return not stack

  def mysolution(self, s:str)->bool:
    stack=[]
    
    for ch in s:
      if ch==')':
        if not stack or stack.pop()!='(':
          return False
      elif ch==']':
        if not stack or stack.pop()!='[':
          return False
      elif ch=='}':
        if not stack or stack.pop()!='{':
          return False
      else:
        stack.append(ch)
    
    return len(stack)==0