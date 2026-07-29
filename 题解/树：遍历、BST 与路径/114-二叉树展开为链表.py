# https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/
# Source: https://walkccc.me/LeetCode/problems/114/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def flatten(self, root: TreeNode | None) -> None:
    if not root:
      return

    self.flatten(root.left)
    self.flatten(root.right)

    left = root.left  # flattened left
    right = root.right  # flattened right

    root.left = None
    root.right = left

    # Connect the original right subtree to the end of the new right subtree.
    rightmost = root
    while rightmost.right:
      rightmost = rightmost.right
    rightmost.right = right
