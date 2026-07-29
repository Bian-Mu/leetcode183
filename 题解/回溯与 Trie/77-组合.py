# https://leetcode.cn/problems/combinations/
# Source: https://walkccc.me/LeetCode/problems/77/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def combine(self, n: int, k: int) -> list[list[int]]:
    ans = []

    def dfs(s: int, path: list[int]) -> None:
      if len(path) == k:
        ans.append(path.copy())
        return

      for i in range(s, n + 1):
        path.append(i)
        dfs(i + 1, path)
        path.pop()

    dfs(1, [])
    return ans
