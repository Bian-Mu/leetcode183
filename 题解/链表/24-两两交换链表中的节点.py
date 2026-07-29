# https://leetcode.cn/problems/swap-nodes-in-pairs/
# Source: https://walkccc.me/LeetCode/problems/24/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def swapPairs(self, head: ListNode) -> ListNode:
    def getLength(head: ListNode) -> int:
      length = 0
      while head:
        length += 1
        head = head.next
      return length

    length = getLength(head)
    dummy = ListNode(0, head)
    prev = dummy
    curr = head

    for _ in range(length // 2):
      next = curr.next
      curr.next = next.next
      next.next = prev.next
      prev.next = next
      prev = curr
      curr = curr.next

    return dummy.next
