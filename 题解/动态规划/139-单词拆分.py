# https://leetcode.cn/problems/word-break/
# Source: https://walkccc.me/LeetCode/problems/139/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def wordBreak(self, s: str, wordDict: list[str]) -> bool:
    wordSet = set(wordDict)

    @functools.lru_cache(None)
    def wordBreak(s: str) -> bool:
      """Returns True if s can be segmented."""
      if s in wordSet:
        return True
      return any(s[:i] in wordSet and wordBreak(s[i:]) for i in range(len(s)))

    return wordBreak(s)

  def mysolution(self, s:str, wordDict: list[str])-> bool:
    wordSet=set(wordDict)
    
    dp=[False for _ in range(len(s)+1)]
    dp[0]=True
    
    for i in range(1,len(s)+1):
      for j in range(1,i+1):
        if dp[j-1] and (s[j-1:i]) in wordSet:
          dp[i]=True
          break
    
    return dp[len(s)]