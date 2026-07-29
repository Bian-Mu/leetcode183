# https://leetcode.cn/problems/rotting-oranges/
# Source algorithm: https://walkccc.me/LeetCode/problems/994/
# SPDX-License-Identifier: MIT
# Python translation of the source algorithm; source copyright (c) 2019-2026 P.-Y. Chen.

from collections import deque


class Solution:
  def orangesRotting(self, grid: list[list[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh = 0
    for r in range(rows):
      for c in range(cols):
        if grid[r][c] == 2:
          queue.append((r, c))
        elif grid[r][c] == 1:
          fresh += 1

    minutes = 0
    for_minutes = ((1, 0), (-1, 0), (0, 1), (0, -1))
    while queue and fresh:
      for _ in range(len(queue)):
        r, c = queue.popleft()
        for dr, dc in for_minutes:
          nr, nc = r + dr, c + dc
          if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
            grid[nr][nc] = 2
            fresh -= 1
            queue.append((nr, nc))
      minutes += 1
    return minutes if fresh == 0 else -1
