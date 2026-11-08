class Solution:
    def solve(self, board: List[List[str]]) -> None:
        #find O's and then do dfs from there

        # if O's are surrounded form all sides by X, then collapse that area do this inplace 
        ROWS , COLS = len(board), len(board[0])

        # helper capture method 
        def capture(r,c): 
            if (r < 0 or c < 0 or r == ROWS or c ==COLS or 
            board[r][c] != "O"): 
                return
            
            board[r][c] = "T"
            capture(r+1, c)
            capture(r-1, c)
            capture(r, c+1)
            capture (r, c-1)

        # capture unsurrounded region (O --> T)
        for r in range(ROWS): 
            for c in range(COLS): 
                if board[r][c] == "O" and (r in [0, ROWS -1] or c in [0, COLS-1]):
                    capture(r,c)

        # capture surrounded regions (O --> X)
        for r in range(ROWS): 
            for c in range(COLS): 
                if board[r][c] == "O": 
                    board[r][c] = "X"

        # uncapture unsurrounded regions (T --> O)
        for r in range(ROWS): 
            for c in range(COLS): 
                if board[r][c] == "T": 
                    board[r][c] = "O"




        