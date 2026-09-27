class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Rule 1: ea row contains 1-9 w/o duplicates
        for row in range(9):
            seen = set()
            for j in range(9):
                if board[row][j] == ".":
                    continue
                if board[row][j] in seen:
                    return False
                seen.add(board[row][j])

        # Rule 2: ea column contains 1-9 w/o duplicates
        for col in range(9):
            seen = set()
            for i in range(9):
                if board[i][col] == ".":
                    continue
                if board[i][col] in seen:
                    return False
                seen.add(board[i][col])

        # Rule 3: ea 3x3 sub box contains 1-9 w/o duplicates
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])

        return True