# https://leetcode.cn/problems/add-two-numbers/
# Source: https://walkccc.me/LeetCode/problems/2/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)
from ListNode import ListNode

class Solution:
  def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode(0)
    curr = dummy
    carry = 0

    while carry or l1 or l2:
      if l1:
        carry += l1.val
        l1 = l1.next
      if l2:
        carry += l2.val
        l2 = l2.next
      curr.next = ListNode(carry % 10)
      carry //= 10
      curr = curr.next

    return dummy.next

  def mysolution(self, l1: ListNode|None, l2: ListNode|None)-> ListNode|None:
    l3=ListNode(0)
    head=l3
    carry:int=0
    
    while l1 and l2:
      sum=l1.val+l2.val+carry
      node=ListNode(sum%10)
      carry=sum//10
      
      l3.next=node
      l3=l3.next
      l1=l1.next
      l2=l2.next
    
    while l1:
      sum=l1.val+carry
      node=ListNode(sum%10)
      carry=sum//10
      
      l3.next=node
      l3=l3.next
      l1=l1.next

    while l2:
      sum=l2.val+carry
      node=ListNode(sum%10)
      carry=sum//10
      
      l3.next=node
      l3=l3.next
      l2=l2.next
      
    if carry:
      l3.next=ListNode(carry)
    
    return head.next