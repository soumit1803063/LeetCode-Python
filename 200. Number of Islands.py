from typing import List,Tuple
from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        rows, cols = len(grid), len(grid[0])

        def bfs(start:Tuple[int]):
            if grid[start[0]][start[1]] =='0' or start in visited:
                return 0
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            queue = deque([start])
            
            while queue:
                r, c = queue.popleft()
                if (r, c) not in visited and 0 <= r < rows and 0 <= c < cols:
                    visited.add((r, c))
                    
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc]=='1' and (nr, nc) not in visited:
                            queue.append((nr, nc))
            
            return 1
        ret = 0
        for i in range(rows):
            for j in range(cols):
               ret+=bfs((i,j))
        return ret 
        