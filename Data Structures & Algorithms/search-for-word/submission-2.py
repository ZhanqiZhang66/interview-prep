class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        DIRS = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = set()

        def backtrack(i, j, path):
            print("".join(path.copy()))
            if "".join(path.copy()) == word:
                print(f"found {path}")
                return True
            if "".join(path.copy()) != word[:len(path)] or len(path) >= len(word):
                print(f"{word[:len(path)]} vs path {path}")
                return False
        
            for dr, dc in DIRS:
                r, c = i + dr, j + dc
                if r in range(ROWS) and c in range(COLS) and (r, c) not in visited:
                    path.append(board[r][c])
                    visited.add((r, c))
                    print(f"trying {path}")
                    if backtrack(r, c, path) == True:
                        return True
                    else:
                        path.pop()
                        visited.remove((r, c))
            return False

        for i in range(ROWS):
            for j in range(COLS):
                print(f"at {i}{j}")
                if backtrack(i, j, [board[i][j]]) == True:
                    
                    return True
        return False
        