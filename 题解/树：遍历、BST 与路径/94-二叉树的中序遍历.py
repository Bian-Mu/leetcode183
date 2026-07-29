# https://leetcode.cn/problems/binary-tree-inorder-traversal/
# Source: https://walkccc.me/LeetCode/problems/94/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def inorderTraversal(self, root: TreeNode | None) -> list[int]:
    ans = []
    stack = []

    while root or stack:
      while root:
        stack.append(root)
        root = root.left
      root = stack.pop()
      ans.append(root.val)
      root = root.right

    return ans
