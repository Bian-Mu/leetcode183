# https://leetcode.cn/problems/sum-root-to-leaf-numbers/
# Source: https://walkccc.me/LeetCode/problems/129/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)
from TreeNode import TreeNode

class Solution:
  def sumNumbers(self, root: TreeNode | None) -> int:
    ans = 0

    def dfs(root: TreeNode | None, path: int) -> None:
      nonlocal ans
      if not root:
        return
      if not root.left and not root.right:
        ans += path * 10 + root.val
        return

      dfs(root.left, path * 10 + root.val)
      dfs(root.right, path * 10 + root.val)

    dfs(root, 0)
    return ans

  def mysolution(self, root: TreeNode|None)->int:
    ans=0
    
    def dfs(node:TreeNode|None,curr:int):
      nonlocal ans
      
      if not node:
        return 
      
      if node and not node.left and not node.right:
        ans+=curr*10+node.val
        return 
      
      dfs(node.left,curr*10+node.val)
      dfs(node.right,curr*10+node.val)  
    
    dfs(root,0)
    return ans