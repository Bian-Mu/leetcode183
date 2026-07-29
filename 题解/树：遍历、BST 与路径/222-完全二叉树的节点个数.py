# https://leetcode.cn/problems/count-complete-tree-nodes/
# Source: https://walkccc.me/LeetCode/problems/222/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def countNodes(self, root: TreeNode | None) -> int:
    if not root:
      return 0
    return 1 + self.countNodes(root.left) + self.countNodes(root.right)
