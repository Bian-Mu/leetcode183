# https://leetcode.cn/problems/generate-parentheses/
# Source: https://walkccc.me/LeetCode/problems/22/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def generateParenthesis(self, n):
    ans = []

    def dfs(l: int, r: int, s: list[str]) -> None:
      if l == 0 and r == 0:
        ans.append(''.join(s))
      if l > 0:
        s.append('(')
        dfs(l - 1, r, s)
        s.pop()
      if l < r:
        s.append(')')
        dfs(l, r - 1, s)
        s.pop()

    dfs(n, n, [])
    return ans

  def mysolution(self, n)->list[str]:
    ans=[]
    
    def dfs(chars: list[str],l,r):
      if l==0 and r==0:
        ans.append(''.join(chars))
        return 
      if l<r:
        chars.append(')')
        dfs(chars,l,r-1)
        chars.pop()
      if l>0:
        chars.append('(')
        dfs(chars,l-1,r)
        chars.pop()
        
      
    dfs([],n,n)
    
    return ans