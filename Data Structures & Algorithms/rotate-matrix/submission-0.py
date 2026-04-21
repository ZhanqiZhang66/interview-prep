class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # horizontal flip= leftside right
        # matrix[:] = [row[::-1] for row in matrix]

        # vertical flip: upside down
        # matrix[:] = matrix[::-1] 

        # both flip
        # matrix[:] = [row[::-1] for row in matrix[::-1]]

        # transpose [i,j] -> [j, i]
        # matrix[:] = [list(row) for row in zip(*matrix)]

        # 90-Degree clockwise = transpose + vertical flip

        # 90-Degree counter clockwise = transpose + horizontal flip 

        matrix[:] = [list(row) for row in zip(*matrix)]
        matrix[:] = [row[::-1] for row in matrix]


        