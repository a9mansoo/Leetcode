from collections import deque
from typing import List

class Solution:

    def __init__(self):
        self.row = 0
        self.col = 0

    def bfs(self, q, grid):

        while q:

            for _ in range(len(q)):
                curr_node = q.popleft()
                i = curr_node[0]
                j = curr_node[1]
                value = curr_node[2]

                left = j - 1
                right = j + 1
                up = i - 1
                down = i + 1

                if (left) >= 0:
                    if grid[i][left] == 2147483647:
                        grid[i][left] = grid[i][j] + 1
                        q.append((i, left, grid[i][left]))
                
                if (right) < self.col:
                    if grid[i][right] == 2147483647:
                        grid[i][right] = grid[i][j] + 1
                        q.append((i, right, grid[i][right]))
                
                if (up) >= 0:
                    if grid[up][j] == 2147483647:
                        grid[up][j] = grid[i][j] + 1
                        q.append((up, j, grid[up][j]))
                
                if (down) < self.row:
                    if grid[down][j] == 2147483647:
                        grid[down][j] = grid[i][j] + 1
                        q.append((down, j, grid[down][j]))
            
            print(grid)



    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        self.row = len(grid)
        self.col = len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    q.append((i, j, 0))
        self.bfs(q, grid)
