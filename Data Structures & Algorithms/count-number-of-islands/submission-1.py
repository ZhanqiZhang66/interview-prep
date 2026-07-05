class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R, C = len(grid), len(grid[0])
        DIRS = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = set()
        def dfs(r, c):
            if r < 0 or r >= R or c < 0 or c >= C or grid[r][c] == '0':
                return
            grid[r][c] = '0'
            for dr, dc in DIRS:
                rr, cc = r + dr, c + dc
                
                dfs(rr, cc)
        res = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == "1":
                    dfs(r, c)
                    res += 1
        return res
        