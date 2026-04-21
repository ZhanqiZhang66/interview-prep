class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        max_area = 0
        DIRS = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(r, c, area):
            # when dfs breaks
            if r < 0 or c < 0 or r > ROWS - 1 or c > COLS - 1 or grid[r][c] == 0:
                return area
            grid[r][c] = 0
            area += 1
            for dr, dc in DIRS:
                area = dfs(r + dr, c + dc, area)
            return area


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = 0
                    max_area = max(max_area,  dfs(r, c, area))
        return max_area

        