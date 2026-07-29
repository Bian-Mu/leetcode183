# https://leetcode.cn/problems/rotate-list/
# Source: https://walkccc.me/LeetCode/problems/61/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def rotateRight(self, head: ListNode, k: int) -> ListNode:
    if not head or not head.next or k == 0:
      return head

    tail = head
    length = 1
    while tail.next:
      tail = tail.next
      length += 1
    tail.next = head  # Circle the list.

    t = length - k % length
    for _ in range(t):
      tail = tail.next
    newHead = tail.next
    tail.next = None

    return newHead
