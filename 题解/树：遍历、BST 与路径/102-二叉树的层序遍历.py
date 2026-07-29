# https://leetcode.cn/problems/binary-tree-level-order-traversal/
# Source: https://walkccc.me/LeetCode/problems/102/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
    if not root:
      return []

    ans = []
    q = collections.deque([root])

    while q:
      currLevel = []
      for _ in range(len(q)):
        node = q.popleft()
        currLevel.append(node.val)
        if node.left:
          q.append(node.left)
        if node.right:
          q.append(node.right)
      ans.append(currLevel)

    return ans
