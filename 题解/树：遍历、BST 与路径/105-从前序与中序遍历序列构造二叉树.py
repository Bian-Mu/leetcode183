# https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# Source: https://walkccc.me/LeetCode/problems/105/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)
from TreeNode import TreeNode

class Solution:
  def buildTree(
      self,
      preorder: list[int],
      inorder: list[int],
  ) -> TreeNode | None:
    inToIndex = {num: i for i, num in enumerate(inorder)}

    def build(
        preStart: int,
        preEnd: int,
        inStart: int,
        inEnd: int,
    ) -> TreeNode | None:
      if preStart > preEnd:
        return None

      rootVal = preorder[preStart]
      rootInIndex = inToIndex[rootVal]
      leftSize = rootInIndex - inStart

      root = TreeNode(rootVal)
      root.left = build(preStart + 1, preStart + leftSize,
                        inStart, rootInIndex - 1)
      root.right = build(preStart + leftSize + 1,
                         preEnd, rootInIndex + 1, inEnd)
      return root

    return build(0, len(preorder) - 1, 0, len(inorder) - 1)

  def mysolution(self, preorder: list[int],inorder: list[int]) -> TreeNode | None:
    if len(preorder)==0:
      return None
    
    node=TreeNode(preorder[0])
    index=inorder.index(node.val)
    node.left=self.mysolution(preorder[1:index+1],inorder[:index])
    node.right=self.mysolution(preorder[index+1:],inorder[index+1:])
    
    return node