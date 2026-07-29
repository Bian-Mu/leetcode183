# https://leetcode.cn/problems/binary-tree-right-side-view/
# Source: https://walkccc.me/LeetCode/problems/199/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def rightSideView(self, root: TreeNode | None) -> list[int]:
    if not root:
      return []

    ans = []
    q = collections.deque([root])

    while q:
      size = len(q)
      for i in range(size):
        root = q.popleft()
        if i == size - 1:
          ans.append(root.val)
        if root.left:
          q.append(root.left)
        if root.right:
          q.append(root.right)

    return ans
