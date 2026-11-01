from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        q = deque()

        # BLOCK 1: Phase 1 Initialization
        for r in range(rows):
            # Hint: This loop must be indented inside the 'r' loop
            for c in range(cols): 
                if grid[r][c] == 0:
                    q.append([r,c])
                    visited.add((r,c))

        # BLOCK 2: Helper Function
        def addneigh(r,c):
            if (r == rows or r < 0 or c == cols or c < 0 or (r,c) in visited or grid[r][c] == -1):
                return
            visited.add((r,c))
            q.append([r, c])

        # BLOCK 3: BFS Traversal
        # Hint: Un-indent this completely so it aligns with 'def addneigh'
        distance = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = distance 
                addneigh(r, c+1)
                addneigh(r+1, c)
                addneigh(r, c-1)
                addneigh(r-1,c)
            distance += 1