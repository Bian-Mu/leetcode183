# https://leetcode.cn/problems/minimum-window-substring/
# Source: https://walkccc.me/LeetCode/problems/76/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def minWindow(self, s: str, t: str) -> str:
    count = collections.Counter(t)
    required = len(t)
    bestLeft = -1
    minLength = len(s) + 1

    l = 0
    for r, c in enumerate(s):
      count[c] -= 1
      if count[c] >= 0:
        required -= 1
      while required == 0:
        if r - l + 1 < minLength:
          bestLeft = l
          minLength = r - l + 1
        count[s[l]] += 1
        if count[s[l]] > 0:
          required += 1
        l += 1

    return '' if bestLeft == -1 else s[bestLeft: bestLeft + minLength]

  def mysolution(self, s:str, t:str)->str:
    chars={}
    for ch in t:
      chars[ch]=chars.get(ch,0)+1
    
    schars={}
    l=0
    r=-1
    bestL= 0
    bestR= len(s)-1
    for i,c in enumerate(s):
      schars[c]=schars.get(c,0)+1
      
      r+=1
      
      while r-l+1>=len(t) and self.match(schars,chars):
        if r-l+1<=bestR-bestL+1:
          bestL=l
          bestR=r
        schars[s[l]]-=1
        l+=1
    
    return s[bestL:bestR+1]        

  def match(self,s,t):
    for key in t:
      if t.get(key)>s.get(key,0):
        return False
    
    return True
  
test=Solution().mysolution('qqwert','wet')
print(test)