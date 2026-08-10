# https://leetcode.cn/problems/same-tree/
# Source: https://walkccc.me/LeetCode/problems/100/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)
from TreeNode import TreeNode

class Solution:
  def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
    if not p or not q:
      return p == q
    return (p.val == q.val and
            self.isSameTree(p.left, q.left) and
            self.isSameTree(p.right, q.right))

  def mysolution(self,p: TreeNode,q: TreeNode)->bool:
    if not p or not q:
      return p==q
    
    return p.val==q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)