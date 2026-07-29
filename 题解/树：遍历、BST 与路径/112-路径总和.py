# https://leetcode.cn/problems/path-sum/
# Source: https://walkccc.me/LeetCode/problems/112/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def hasPathSum(self, root: TreeNode, summ: int) -> bool:
    if not root:
      return False
    if root.val == summ and not root.left and not root.right:
      return True
    return (self.hasPathSum(root.left, summ - root.val) or
            self.hasPathSum(root.right, summ - root.val))
