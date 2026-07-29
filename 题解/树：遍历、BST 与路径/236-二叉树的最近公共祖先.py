# https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/
# Source: https://walkccc.me/LeetCode/problems/236/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def lowestCommonAncestor(
      self,
      root: 'TreeNode',
      p: 'TreeNode',
      q: 'TreeNode',
  ) -> 'TreeNode':
    if not root or root == p or root == q:
      return root
    left = self.lowestCommonAncestor(root.left, p, q)
    right = self.lowestCommonAncestor(root.right, p, q)
    if left and right:
      return root
    return left or right
