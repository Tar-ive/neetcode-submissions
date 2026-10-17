class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()

        #base case where we return 1
        def dfs(i,j): #passing in coordinates 
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
                return 1
        # base case where we return 0
            if (i,j) in visited: 
                return 0 
        # add to perimiter
            visited.add((i,j))
            perim = dfs(i, j+1)
            perim += dfs(i+1, j)
            perim += dfs(i, j-1)
            perim += dfs(i-1, j)

            return perim
        # call dfs helper function 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    return dfs(i,j)
        