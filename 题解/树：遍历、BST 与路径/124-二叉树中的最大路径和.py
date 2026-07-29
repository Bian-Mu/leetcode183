# https://leetcode.cn/problems/binary-tree-maximum-path-sum/
# Source: https://walkccc.me/LeetCode/problems/124/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def maxPathSum(self, root: TreeNode | None) -> int:
    ans = -math.inf

    def maxPathSumDownFrom(root: TreeNode | None) -> int:
      """
      Returns the maximum path sum starting from the current root, where
      root.val is always included.
      """
      nonlocal ans
      if not root:
        return 0

      l = max(0, maxPathSumDownFrom(root.left))
      r = max(0, maxPathSumDownFrom(root.right))
      ans = max(ans, root.val + l + r)
      return root.val + max(l, r)

    maxPathSumDownFrom(root)
    return ans
