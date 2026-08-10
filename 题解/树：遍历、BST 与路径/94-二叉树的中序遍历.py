# https://leetcode.cn/problems/binary-tree-inorder-traversal/
# Source: https://walkccc.me/LeetCode/problems/94/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)
from TreeNode import TreeNode,convert

class Solution:
  def inorderTraversal(self, root: TreeNode | None) -> list[int]:
    ans = []
    stack = []

    while root or stack:
      while root:
        stack.append(root)
        root = root.left
      root = stack.pop()
      ans.append(root.val)
      root = root.right

    return ans

  def mysolution(self, root: TreeNode|None)-> list[int]:
    def calc(node:TreeNode|None):
      if node is None:
        return []
      
      return calc(node.left)+[node.val]+calc(node.right)
    
    return calc(root)

t=convert([1,2,3,4,None,6])
print(Solution().mysolution(t))