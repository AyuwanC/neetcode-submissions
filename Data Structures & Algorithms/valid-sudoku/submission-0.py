class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            unique1 = set()
            unique2 = set()
            unique3 = set()

            for j in range(9):
                if board[i][j] != '.' and (board[i][j] in unique1):
                    return False
                else:
                    unique1.add(board[i][j])

                if board[j][i] != '.' and (board[j][i] in unique2):
                    return False
                else:
                    unique2.add(board[j][i])
                    
                if board[3*(i//3) + j//3][3*(i%3) + j%3] != '.' and (board[3*(i//3) + j//3][3*(i%3) + j%3] in unique3):
                    return False
                else:
                    unique3.add(board[3*(i//3) + j//3][3*(i%3) + j%3])
        return True
                