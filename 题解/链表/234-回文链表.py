# https://leetcode.cn/problems/palindrome-linked-list/
# Source: https://walkccc.me/LeetCode/problems/234/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def isPalindrome(self, head: ListNode) -> bool:
    def reverseList(head: ListNode) -> ListNode:
      prev = None
      curr = head
      while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
      return prev

    slow = head
    fast = head

    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next

    if fast:
      slow = slow.next
    slow = reverseList(slow)

    while slow:
      if slow.val != head.val:
        return False
      slow = slow.next
      head = head.next

    return True
