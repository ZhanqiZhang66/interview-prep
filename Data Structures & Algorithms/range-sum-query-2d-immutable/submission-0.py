class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.R = len(matrix)
        self.C = len(matrix[0])
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 < 0 or row1 > self.R or col1 < 0 or col1 > self.C or row2 < 0 or row2 > self.R or col2 < 0 or col2 > self.C:
            return 0
        res = 0
        for r in range(row1, row2 + 1):
            for c in range(col1, col2 + 1):
                res += self.matrix[r][c]
        return res
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)