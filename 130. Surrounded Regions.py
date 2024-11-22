from typing import List,Tuple
from collections import deque
class Solution:
    def solve(self, grid: List[List[str]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        for r in range(rows):
            if grid[r][0]=='O':
                self.dfs(grid, r,0)

            if grid[r][cols-1]=='O':
                self.dfs(grid, r,cols-1)
        
        for c in range(cols):
            if grid[0][c]=='O':
                self.dfs(grid, 0,c)

            if grid[rows-1][c]=='O':
                self.dfs(grid, rows-1,c)

        for r,row in enumerate(grid):
            for c,cell in enumerate(row):
                if cell == 'n':
                    grid[r][c]='O'
                else:
                    grid[r][c]='X'

    def dfs(self,grid,r,c):
        rows = len(grid)
        cols = len(grid[0])

        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != 'O':
            return
        grid[r][c]='n'
        self.dfs(grid,r-1,c)
        self.dfs(grid,r+1,c)
        self.dfs(grid,r,c-1)
        self.dfs(grid,r,c+1)
        
        