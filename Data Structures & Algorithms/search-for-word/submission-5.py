class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        DIRS = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        if len(word) > ROWS * COLS:
            return False

        def backtrack(i, j, k):
            if k == len(word):
                return True
            if word[k] != board[i][j] or board[i][j] == '#':
                return False
            
 
            board[i][j] = '#'        
            for dr, dc in DIRS:
                r, c = i + dr, j + dc
                if r in range(ROWS) and c in range(COLS):
                    if backtrack(r, c, k+1) == True:
                        return True
            board[i][j] = word[k]
            return False

        for i in range(ROWS):
            for j in range(COLS):
                if backtrack(i, j, 0):  
                    return True
        return False
        