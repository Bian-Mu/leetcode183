# https://leetcode.cn/problems/maximum-depth-of-binary-tree/
# Source: https://walkccc.me/LeetCode/problems/104/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def maxDepth(self, root: TreeNode | None) -> int:
    if not root:
      return 0
    return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
