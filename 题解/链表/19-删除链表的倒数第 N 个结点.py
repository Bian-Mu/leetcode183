# https://leetcode.cn/problems/remove-nth-node-from-end-of-list/
# Source: https://walkccc.me/LeetCode/problems/19/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

from ListNode import ListNode,convert

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

  def mysolution(self, head: ListNode, n:int)-> ListNode|None:
    curr=head
    cnt=0
    
    while curr:
      curr=curr.next
      cnt+=1
    
    if cnt<n:
      return None 
    
    curr=head
    n=cnt-n
    if not n:
      return head.next
    
    
    while n and curr:
      pre=curr
      curr=curr.next
      n-=1
      
      if not n:
        pre.next=curr.next
    
    return head
  
l=convert([1,2,3,4,5])
tmp=Solution()
print(tmp.mysolution(l,3))