# https://leetcode.cn/problems/invert-binary-tree/
# Source: https://walkccc.me/LeetCode/problems/226/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def invertTree(self, root: TreeNode | None) -> TreeNode | None:
    if not root:
      return None

    left = root.left
    right = root.right
    root.left = self.invertTree(right)
    root.right = self.invertTree(left)
    return root
