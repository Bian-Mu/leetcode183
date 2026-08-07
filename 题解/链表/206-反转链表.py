# https://leetcode.cn/problems/reverse-linked-list/
# Source: https://walkccc.me/LeetCode/problems/206/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)
from ListNode import ListNode,convert

class Solution:
  def reverseList(self, head: ListNode | None) -> ListNode | None:
    if not head or not head.next:
      return head

    newHead = self.reverseList(head.next)
    head.next.next = head
    head.next = None
    return newHead

  def mysolution(self, head: ListNode|None)-> ListNode|None:
    if not head or not head.next:
      return head
    
    dummy=ListNode(0,head)
    pre=dummy
    curr=head
    
    while curr and curr.next:
      next=curr.next
      curr.next=next.next
      next.next=pre.next
      pre.next=next
    
    
    return dummy.next

l=convert([1,2,3,4,5])
print(Solution().mysolution(l))