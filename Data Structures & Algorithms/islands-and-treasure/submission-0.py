class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2**31 - 1 
        DIRS = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        ROWS, COLS = len(grid), len(grid[0])

        queue = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append([r,c])
        while queue:
          
            rr, cc = queue.popleft()
            for dr, dc in DIRS:
                n_r, n_c = rr + dr, cc + dc
                if 0 <= n_r <= ROWS-1 and 0 <= n_c <= COLS-1 and grid[n_r][n_c] == INF:
                    grid[n_r][n_c] = 1 + grid[rr][cc] 
                    queue.append([n_r, n_c])
        

        # def bfs(r, c):
        #     # 3 init
        #     queue = deque([(r, c)])
        #     visited = {(r, c)}
        #     ans = 0

        #     while queue:
        #         for _ in range(len(queue)):
        #             # 1. pop me
        #             rr, cc = queue.popleft()
        #             # 2. do logic
        #             if grid[rr][cc] == 0:
        #                 return ans
        #             # 3. add my unvisited neighbor
        #             for dr, dc in DIRS:
        #                 row = rr + dr
        #                 col = cc + dc
        #                 if (row, col) not in visited and 0 <= row <= ROWS -1 and 0 <= col <= COLS -1 and grid[row][col] != -1:
        #                     visited.add((row, col))
        #                     queue.append((row, col))
        #         ans += 1
        #     return INF

        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if grid[r][c] == INF:
        #             ans = bfs(r, c)
        #             grid[r][c] = ans

        