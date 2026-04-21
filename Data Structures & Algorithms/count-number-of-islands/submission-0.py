class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        DIR = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        connected_components = 0

        def dfs(r, c):
            if (r < 0 or c < 0 or r > ROW-1 or c > COL-1 or grid[r][c] == "0"):
                return
            grid[r][c] = "0"

            for dr, dc in DIR:
                dfs(r + dr, c + dc)

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == "1":
                    dfs(r, c)
                    connected_components += 1
        return connected_components


        