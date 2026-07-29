# https://leetcode.cn/problems/copy-list-with-random-pointer/
# Source: https://walkccc.me/LeetCode/problems/138/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def copyRandomList(self, head: 'Node') -> 'Node':
    if not head:
      return None
    if head in self.map:
      return self.map[head]

    newNode = Node(head.val)
    self.map[head] = newNode
    newNode.next = self.copyRandomList(head.next)
    newNode.random = self.copyRandomList(head.random)
    return newNode

  map = {}
