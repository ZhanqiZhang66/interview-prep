class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        DIRS = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        # start from boarder Os inward, if see a O next to O, this O cannot be flipped
        queue = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if (r == 0 or r == ROWS - 1 or c == 0 or c == COLS - 1) and board[r][c] == 'O':
                    queue.append((r, c))
        while queue:
            r, c = queue.pop()
            if board[r][c] == 'O':
                board[r][c] = 'T'
            for dr, dc in DIRS:
                rr = r + dr
                cc = c + dc
                if rr in range(1, ROWS-1) and cc in range(1, COLS-1) and board[rr][cc] == 'O':
                    queue.append((rr, cc))


        # #the Os cannot be flipped -> )
        # the rest Os -> X
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                if board[r][c] == 'T':
                    board[r][c] = 'O'
        
        