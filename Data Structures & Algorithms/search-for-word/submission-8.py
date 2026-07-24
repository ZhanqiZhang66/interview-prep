class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW, COL = len(board), len(board[0])
        DIRS = [[0, 1], [0, -1], [1, 0], [-1, 0]]


        def dfs(board, i, j, s, k):
            # basecase
            if k == len(word):
                return True
            if i < 0 or i > ROW -1 or j < 0 or j > COL -1 or board[i][j] == "#" or k > len(word) or board[i][j] != word[k]:
                return False
            tmp = board[i][j]
            board[i][j] = "#"

            found =  dfs(board, i + 0, j + 1, s+board[i][j], k+1) or dfs(board, i + 0, j - 1, s+board[i][j], k+1) or dfs(board, i + 1, j + 0, s+board[i][j], k+1) or dfs(board, i - 1, j + 0, s+board[i][j], k+1)
           
            board[i][j] = tmp
            return found
   
        # backtrack
        for r in range(ROW):
            for c in range(COL):
                if dfs(board, r, c, "", 0):
                    return True
        return False

        