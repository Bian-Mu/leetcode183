# https://leetcode.cn/problems/intersection-of-two-linked-lists/
# Source: https://walkccc.me/LeetCode/problems/160/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def getIntersectionNode(
      self,
      headA: ListNode,
      headB: ListNode,
  ) -> ListNode | None:
    a = headA
    b = headB

    while a != b:
      a = a.next if a else headB
      b = b.next if b else headA

    return a
