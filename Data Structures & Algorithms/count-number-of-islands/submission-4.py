class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # do dfs 

        # count no of islands

        visited = set()

        # visited set for positions visited

        # recursive dfs call

        def dfs(i,j): 
            if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0 or (i,j) in visited or grid[i][j] == "0":
                return

            visited.add((i,j))   
            dfs(i,j+1)
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j-1)

        islands = 0 
        for i in range(len(grid)): 
            for j in range(len(grid[0])): 
                if (i,j) not in visited and grid[i][j] == "1": 
                    dfs(i,j)
                    islands +=1 
        
        return islands

        



        

        