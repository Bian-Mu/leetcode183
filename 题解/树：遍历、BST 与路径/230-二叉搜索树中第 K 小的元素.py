# https://leetcode.cn/problems/kth-smallest-element-in-a-bst/
# Source: https://walkccc.me/LeetCode/problems/230/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)
from TreeNode import TreeNode


class Solution:
  def kthSmallest(self, root: TreeNode | None, k: int) -> int:
    def countNodes(root: TreeNode | None) -> int:
      if not root:
        return 0
      return 1 + countNodes(root.left) + countNodes(root.right)

    leftCount = countNodes(root.left)

    if leftCount == k - 1:
      return root.val
    if leftCount >= k:
      return self.kthSmallest(root.left, k)
    return self.kthSmallest(root.right, k - 1 - leftCount)  # leftCount < k

  def mysolution(self ,root: TreeNode|None, k:int)->int:
    stack=[]
    while stack or root:
      while root:
        stack.append(root)
        root=root.left
      root=stack.pop()
      k-=1
      if not k:
        return root.val
      root=root.right