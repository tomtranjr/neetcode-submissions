class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # brute force:
        # for r in range(len(matrix)):
        #     for c in range(len(matrix[0])):
        #         if matrix[r][c] == target:
        #             return True
        # return False

        # two pointer (one pass)
        ROWS, COLS = len(matrix), len(matrix[0])

        l, r = 0, ROWS * COLS - 1

        while l <= r:
            m = l + (r - l) // 2
            row, col = m // COLS, m % COLS
            if matrix[row][col] < target:
                l = m + 1
            elif matrix[row][col] > target:
                r = m - 1
            else:
                return True
        return False