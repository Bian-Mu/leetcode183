# https://leetcode.cn/problems/sum-root-to-leaf-numbers/
# Source: https://walkccc.me/LeetCode/problems/129/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def sumNumbers(self, root: TreeNode | None) -> int:
    ans = 0

    def dfs(root: TreeNode | None, path: int) -> None:
      nonlocal ans
      if not root:
        return
      if not root.left and not root.right:
        ans += path * 10 + root.val
        return

      dfs(root.left, path * 10 + root.val)
      dfs(root.right, path * 10 + root.val)

    dfs(root, 0)
    return ans
