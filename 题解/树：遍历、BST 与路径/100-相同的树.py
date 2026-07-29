# https://leetcode.cn/problems/same-tree/
# Source: https://walkccc.me/LeetCode/problems/100/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
    if not p or not q:
      return p == q
    return (p.val == q.val and
            self.isSameTree(p.left, q.left) and
            self.isSameTree(p.right, q.right))
