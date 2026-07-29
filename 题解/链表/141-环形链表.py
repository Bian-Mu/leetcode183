# https://leetcode.cn/problems/linked-list-cycle/
# Source: https://walkccc.me/LeetCode/problems/141/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def hasCycle(self, head: ListNode) -> bool:
    slow = head
    fast = head

    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next
      if slow == fast:
        return True

    return False
