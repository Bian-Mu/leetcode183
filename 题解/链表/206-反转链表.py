# https://leetcode.cn/problems/reverse-linked-list/
# Source: https://walkccc.me/LeetCode/problems/206/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def reverseList(self, head: ListNode | None) -> ListNode | None:
    if not head or not head.next:
      return head

    newHead = self.reverseList(head.next)
    head.next.next = head
    head.next = None
    return newHead
