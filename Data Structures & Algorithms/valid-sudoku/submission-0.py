class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        R, C = len(board), len(board[0])
        for r in range(R):
            c = Counter(board[r][:])
            for k, v in c.items():
                if k != "." and v > 1:
                    return False
        for col in range(R):
            c = Counter(board[:][col])
            for k, v in c.items():
                if k != "." and v > 1:
                    return False

        for i in range(3):
            for j in range(3):
                box = [
                    board[r][c]
                    for r in range(i*3, i*3+3)
                    for c in range(j*3, j*3+3)
                ]
                print(box)
                print(f"{i*3} {i*3+3} {j*3} {j*3+3}")
                c = Counter(box)
                for k, v in c.items():
                    if k != "." and v > 1:
                        return False
        return True


        