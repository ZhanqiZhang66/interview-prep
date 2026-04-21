class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        R, C = len(board), len(board[0])
        rows = defaultdict(list)
        cols = defaultdict(list)
        sqs = defaultdict(list)

        for r in range(R):
            for c in range(C):
                val = board[r][c]
                if val == ".":
                    continue
                if val in rows[r] or val in cols[c] or val in sqs[(r//3, c//3)]:
                    return False
                rows[r].append(val)
                cols[c].append(val)
                sqs[(r//3, c//3)].append(val)
        return True


        