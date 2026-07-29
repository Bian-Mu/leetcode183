# https://leetcode.cn/problems/minimum-absolute-difference-in-bst/
# Source algorithm: https://walkccc.me/LeetCode/problems/530/
# SPDX-License-Identifier: MIT
# Python translation of the source algorithm; source copyright (c) 2019-2026 P.-Y. Chen.

class Solution:
  def getMinimumDifference(self, root: 'Optional[TreeNode]') -> int:
    previous = None
    answer = float('inf')

    def inorder(node: 'Optional[TreeNode]') -> None:
      nonlocal previous, answer
      if not node:
        return
      inorder(node.left)
      if previous is not None:
        answer = min(answer, node.val - previous)
      previous = node.val
      inorder(node.right)

    inorder(root)
    return answer
