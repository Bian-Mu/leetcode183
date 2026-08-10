# https://leetcode.cn/problems/validate-binary-search-tree/
# Source: https://walkccc.me/LeetCode/problems/98/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)
from TreeNode import TreeNode

class Solution:
  def isValidBST(self, root: TreeNode | None) -> bool:
    def isValidBST(root: TreeNode | None,
                   minNode: TreeNode | None, maxNode: TreeNode | None) -> bool:
      if not root:
        return True
      if minNode and root.val <= minNode.val:
        return False
      if maxNode and root.val >= maxNode.val:
        return False

      return (isValidBST(root.left, minNode, root) and
              isValidBST(root.right, root, maxNode))

    return isValidBST(root, None, None)

  def mysolution(self, root: TreeNode| None)->bool:
    minVal=float('inf')
    queue=[]
    
    while queue or root:
      while root:
        queue.append(root)
        root=root.left
      node=queue.pop()
      if minVal==float('inf'):
        minVal=node.val
      elif node.val<=minVal:
        return False
      else:
        minVal=node.val
      root=node.right
    
    return True