class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # each row and col can be a set. 
        # each of the 3 x 3 sub-boxes should be a dictionary. 

        # we return true if all rows and cols dont contain duplicates
        # and all 3 x 3 sub-boxes dont contain duplicate 
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):  
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or 
                    board[r][c] in squares[(r//3,c//3)]):
                    return False 
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3,c//3)].add(board[r][c])

        return True