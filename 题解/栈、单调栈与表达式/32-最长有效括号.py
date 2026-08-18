# https://leetcode.cn/problems/longest-valid-parentheses/
# Source: https://walkccc.me/LeetCode/problems/32/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def longestValidParentheses(self, s: str) -> int:
    s2 = ')' + s
    # dp[i] := the length of the longest valid parentheses in the substring
    # s2[1..i]
    dp = [0] * len(s2)

    for i in range(1, len(s2)):
      if s2[i] == ')' and s2[i - dp[i - 1] - 1] == '(':
        dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2

    return max(dp)

  def mysolution(self, s:str)-> int:
    dp=[0]*len(s)
    
    for i in range(1,len(s)):
      if s[i]==')':
        if i-dp[i-1]-1>=0 and s[i-dp[i-1]-1]=='(':
          dp[i]=dp[i-1]+2
        if i-dp[i-1]-2>=0:
          dp[i]+=dp[i-dp[i-1]-2]
    
    return max(dp)