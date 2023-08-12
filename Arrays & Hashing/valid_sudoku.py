# 36. Valid Sudoku
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Time:O(n^2), Memory: O(n)
        def checkRows(board:List[List[str]])->bool:
            for r in board:
                mp={}
                for el in r:
                    if el==".":
                        continue
                    else:
                        if el in mp:
                            return False
                        else:
                            mp[el]=True
            return True
        
        # Time: O(n^2), Memory: O(n)
        def checkCols(board:List[List[str]])->bool:
            for c in range(0,len(board)):
                mp={}
                for r in range(0,len(board)):
                    if board[r][c]==".":
                        continue
                    else:
                        if board[r][c] in mp:
                            return False
                        else:
                            mp[board[r][c]]=True
            return True
        # Time: O(n^2), Memory: O(n)
        def checkBox(board:List[List[str]])->bool:
            for i in range(0, 9, 3):
                for j in range(0, 9, 3):
                    mp = {}
                    for r in range(i, i + 3):
                        for c in range(j, j + 3):
                            if board[r][c] == ".":
                                continue
                            else:
                                if board[r][c] in mp:
                                    return False
                                else:
                                    mp[board[r][c]] = True
            return True

        return checkRows(board) and checkBox(board) and checkCols(board)