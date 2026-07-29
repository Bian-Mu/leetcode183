# https://leetcode.cn/problems/path-sum-iii/
# Source: https://walkccc.me/LeetCode/problems/437/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def pathSum(self, root: TreeNode | None, summ: int) -> int:
    if not root:
      return 0

    def dfs(root: TreeNode, summ: int) -> int:
      if not root:
        return 0
      return (int(summ == root.val) +
              dfs(root.left, summ - root.val) +
              dfs(root.right, summ - root.val))

    return (dfs(root, summ) +
            self.pathSum(root.left, summ) +
            self.pathSum(root.right, summ))
