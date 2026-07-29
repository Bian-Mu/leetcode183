# https://leetcode.cn/problems/longest-common-prefix/
# Source: https://walkccc.me/LeetCode/problems/14/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def longestCommonPrefix(self, strs: list[str]) -> str:
    if not strs:
      return ''

    for i in range(len(strs[0])):
      for j in range(1, len(strs)):
        if i == len(strs[j]) or strs[j][i] != strs[0][i]:
          return strs[0][:i]

    return strs[0]
