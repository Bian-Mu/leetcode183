# https://leetcode.cn/problems/remove-nth-node-from-end-of-list/
# Source: https://walkccc.me/LeetCode/problems/19/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    slow = head
    fast = head

    for _ in range(n):
      fast = fast.next
    if not fast:
      return head.next

    while fast.next:
      slow = slow.next
      fast = fast.next
    slow.next = slow.next.next

    return head
