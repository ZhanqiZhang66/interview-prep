class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        r = 0
        c = COLS - 1

        left = [0, 0]
        right = [ROWS - 1, COLS - 1]

        while left[0] < right[0] and left[1] < right[1]:
            while left[0] != right[0]:
                mid = [left[0], right[1]]
                mid_val = matrix[mid[0]][mid[1]]
                print(f"at mid {left[0]} {right[1]}, mid_val={mid_val}")
                if mid_val == target:
                    return True
                elif target > mid_val:
                    left[0] = mid[0] + 1
                    print(f"update left {left} and right = {right}")
                else:
                    right[0] = mid[0]
                    print(f"update right {right}, and left = {left}")
            
            row = left[0]
            l = left[1]
            r = right[1]
            print(f"at row{row}, l={l}, r={r}")
            while l < r:
                mid_col = (l + r) // 2
                mid_val = matrix[row][mid_col]
                print(f"at row{row}, [{l}, {r}], mid={mid_col} and val = {mid_val}")
                if mid_val == target:
                    return True
                elif target > mid_val:
                    l = mid_col + 1
                    print(f"at row{row}, l={l}")
                else:
                    r = mid_col - 1
                    print(f"at row{row}, r={r}")
            return True if matrix[row][l] == target else False
        return False
        