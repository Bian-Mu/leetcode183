# https://leetcode.cn/problems/average-of-levels-in-binary-tree/
# Source algorithm: https://walkccc.me/LeetCode/problems/637/
# SPDX-License-Identifier: MIT
# Python translation of the source algorithm; source copyright (c) 2019-2026 P.-Y. Chen.

from collections import deque


class Solution:
  def averageOfLevels(self, root: 'Optional[TreeNode]') -> list[float]:
    answer = []
    queue = deque([root])
    while queue:
      level_size = len(queue)
      total = 0
      for _ in range(level_size):
        node = queue.popleft()
        total += node.val
        if node.left:
          queue.append(node.left)
        if node.right:
          queue.append(node.right)
      answer.append(total / level_size)
    return answer
