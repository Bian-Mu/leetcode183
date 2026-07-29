# https://leetcode.cn/problems/group-anagrams/
# Source: https://walkccc.me/LeetCode/problems/49/
# SPDX-License-Identifier: MIT
# Copyright (c) 2019-2026 P.-Y. Chen (walkccc)

class Solution:
  def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
    dict = collections.defaultdict(list)

    for str in strs:
      key = ''.join(sorted(str))
      dict[key].append(str)

    return dict.values()
