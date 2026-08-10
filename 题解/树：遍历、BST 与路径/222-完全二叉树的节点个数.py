# https://leetcode.cn/problems/count-complete-tree-nodes/
# Source: https://walkccc.me/LeetCode/problems/222/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)
from TreeNode import TreeNode

class Solution:
  def countNodes(self, root: TreeNode | None) -> int:
    if not root:
      return 0
    return 1 + self.countNodes(root.left) + self.countNodes(root.right)

  def mysolution(self, root: TreeNode|None)->int:
    def calc(node:TreeNode|None):
      if not node:
        return 0
      return 1+max(calc(node.left),calc(node.right))
    if not root:
      return 0
    
    ld,rd=calc(root.left),calc(root.right)
    if ld==rd:
      return 1+2**(ld+1)-2
    elif ld>rd:
      return self.mysolution(root.left)+2**rd-1+1
    else:
      return self.mysolution(root.right)+2**ld-1+1