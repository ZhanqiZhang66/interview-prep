class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        R, C = len(matrix), len(matrix[0])
        DIRs = [[0, 1], ]

        def dfs(r, c):
            if matrix[r][c] != 0 or r not in range(R) or c not in range(C):
                return

            for col in range(C):
                matrix[r][col] = '#'
            for row in range(R):
                matrix[row][c] = '#'

        for r in range(R):
            for c in range(C):
                dfs(r, c)

        for r in range(R):
            for c in range(C):
                if matrix[r][c] == '#':
                    matrix[r][c] = 0


        
        