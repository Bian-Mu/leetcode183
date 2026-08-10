# https://leetcode.cn/problems/symmetric-tree/
# Source: https://walkccc.me/LeetCode/problems/101/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)
from TreeNode import TreeNode

class Solution:
  def isSymmetric(self, root: TreeNode | None) -> bool:
    def isSymmetric(p: TreeNode | None, q: TreeNode | None) -> bool:
      if not p or not q:
        return p == q
      return (p.val == q.val and
              isSymmetric(p.left, q.right) and
              isSymmetric(p.right, q.left))

    return isSymmetric(root, root)

  def mysolution(self,root: TreeNode)->bool:
    def calc(p: TreeNode,q: TreeNode):
      if not p or not q:
        return p==q
      return p.val==q.val and calc(p.left,q.right) and calc(p.right,q.left)
    
    if not root:
      return True
    return calc(root.left,root.right)