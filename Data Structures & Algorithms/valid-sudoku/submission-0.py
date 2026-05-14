class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = {str(i): False for i in range(1, 10)}
        row["."] = True 
        col = {str(i): False for i in range(1, 10)}
        col["."] = True 
        grid = {str(i): False for i in range(1, 10)}
        grid["."] = True 

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if row[num] is True and num != ".":
                    return False 
                row[num] = True 

                num = board[j][i]
                if col[num] is True and num != ".":
                    return False 
                col[num] = True 
               
            row = {str(i): False for i in range(1, 10)}
            row["."] = True 
            col = {str(i): False for i in range(1, 10)}
            col["."] = True 

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                for k in range(i, i+3):
                    for l in range(j, j+3):
                        num = board[k][l]
                        if grid[num] is True and num != ".":
                            return False 
                        grid[num] = True 

                grid = {str(i): False for i in range(1, 10)}
                grid["."] = True 

        return True 