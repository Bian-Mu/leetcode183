# https://leetcode.cn/problems/subsets/
# Source: https://walkccc.me/LeetCode/problems/78/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def subsets(self, nums: list[int]) -> list[list[int]]:
    ans = []

    def dfs(s: int, path: list[int]) -> None:
      ans.append(path)

      for i in range(s, len(nums)):
        dfs(i + 1, path + [nums[i]])

    dfs(0, [])
    return ans

  def mysolution(self, nums: list[int])-> list[list[int]]:
    ans=[]
    
    def dfs(index,path):
      if index==len(nums):
        ans.append(path.copy())
        return 
      
      dfs(index+1,path+[nums[index]])
      dfs(index+1,path)
    
    dfs(0,[])
    
    return ans

test=Solution().mysolution([1,2,3])
print(test)