# https://leetcode.cn/problems/diameter-of-binary-tree/
# Source: https://walkccc.me/LeetCode/problems/543/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def diameterOfBinaryTree(self, root: TreeNode | None) -> int:
    ans = 0

    def maxDepth(root: TreeNode | None) -> int:
      nonlocal ans
      if not root:
        return 0

      l = maxDepth(root.left)
      r = maxDepth(root.right)
      ans = max(ans, l + r)
      return 1 + max(l, r)

    maxDepth(root)
    return ans
