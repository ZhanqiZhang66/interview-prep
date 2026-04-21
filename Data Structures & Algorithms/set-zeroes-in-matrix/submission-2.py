class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        R, C = len(matrix), len(matrix[0])

        row_zero = 1
        for r in range(R):
            for c in range(C):
                if matrix[r][c] == 0:
                    if r == 0:
                        row_zero = 0
                    else:
                        matrix[r][0] = 0
                    matrix[0][c] = 0

        for r in range(1, R):
            for c in range(1, C):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        if matrix[0][0] == 0:
            for r in range(R):
                matrix[r][0] = 0
        if row_zero == 0:
            for c in range(C):
                matrix[0][c] = 0