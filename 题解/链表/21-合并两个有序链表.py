# https://leetcode.cn/problems/merge-two-sorted-lists/
# Source: https://walkccc.me/LeetCode/problems/21/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

from ListNode import ListNode

class Solution:
  def mergeTwoLists(
      self,
      list1: ListNode | None,
      list2: ListNode | None,
  ) -> ListNode | None:
    if not list1 or not list2:
      return list1 if list1 else list2
    if list1.val > list2.val:
      list1, list2 = list2, list1
    list1.next = self.mergeTwoLists(list1.next, list2)
    return list1

  def mysolution(self, list1: ListNode|None, list2: ListNode|None)->ListNode|None:
    head=ListNode(0)
    curr=head
    
    while list1 or list2:
      if list1 and list2:
        if list1.val>list2.val:
          curr.next=list2
          list2=list2.next
        else:
          curr.next=list1
          list1=list1.next
        curr=curr.next
      elif list1:
        curr.next=list1
        break
      else:
        curr.next=list2
        break 

    return head.next