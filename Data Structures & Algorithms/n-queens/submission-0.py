class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        board = [["."] * n for _ in range(n)]
        cols = set()
        posDia = set() # r + c 
        negDia = set() # r - c 
        
        def backtrack(r):
            if r == n:
                board_copy = ["".join(row) for row in board.copy()]    
                ans.append(board_copy)
                return

            for c in range(n):
                if c in cols or (r+c) in posDia or (r-c) in negDia:
                    continue
                
                board[r][c] = "Q"
                cols.add(c)
                posDia.add(r + c)
                negDia.add(r - c)

                backtrack(r+1)

                board[r][c] = "."
                cols.remove(c)
                posDia.remove(r + c)
                negDia.remove(r - c)
        backtrack(0)
        return ans



            

            

           