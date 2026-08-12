# https://leetcode.cn/problems/binary-tree-maximum-path-sum/
# Source: https://walkccc.me/LeetCode/problems/124/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)
from TreeNode import TreeNode

class Solution:
  def maxPathSum(self, root: TreeNode | None) -> int:
    ans = -math.inf

    def maxPathSumDownFrom(root: TreeNode | None) -> int:
      """
      Returns the maximum path sum starting from the current root, where
      root.val is always included.
      """
      nonlocal ans
      if not root:
        return 0

      l = max(0, maxPathSumDownFrom(root.left))
      r = max(0, maxPathSumDownFrom(root.right))
      ans = max(ans, root.val + l + r)
      return root.val + max(l, r)

    maxPathSumDownFrom(root)
    return ans

  def mysolution(self, root: TreeNode)->int:
    ans=-float('inf')
    def dfs(node:TreeNode|None)->int:
      if not node:
        return 0
      
      nonlocal ans
      
      l=max(0,dfs(node.left))
      r=max(0,dfs(node.right))
      ans=max(ans,node.val+l+r)
      return node.val+max(l,r)
      
    dfs(root)
    
    return ans  