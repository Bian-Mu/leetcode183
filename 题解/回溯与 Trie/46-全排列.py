# https://leetcode.cn/problems/permutations/
# Source: https://walkccc.me/LeetCode/problems/46/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def permute(self, nums: list[int]) -> list[list[int]]:
    ans = []
    used = [False] * len(nums)

    def dfs(path: list[int]) -> None:
      if len(path) == len(nums):
        ans.append(path.copy())
        return

      for i, num in enumerate(nums):
        if used[i]:
          continue
        used[i] = True
        path.append(num)
        dfs(path)
        path.pop()
        used[i] = False

    dfs([])
    return ans

  def mysolution(self, nums: list[int])-> list[list[int]]:
    ans=[]
    
    def dfs(index,path):
      if index==len(nums):
        ans.append(path.copy())
        return 
      
      for i in range(index,len(nums)):
        nums[index],nums[i]=nums[i],nums[index]
        dfs(index+1,nums)
        nums[index],nums[i]=nums[i],nums[index]
      
    dfs(0,nums)
    
    return ans
  
test=Solution().mysolution([1,2,3])
print(test)