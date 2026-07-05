class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        R, C = len(grid), len(grid[0])
        DIRS = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = set()
        res = 0

        def dfs(r, c):
            nonlocal res
            if r < 0 or r >= R or c < 0 or c >= C or grid[r][c] == 0:
                return 1
            if (r, c) in visited:
                return 0
            visited.add((r, c))
            perimeter = 0
            for dr, dc in DIRS:
                rr, cc = r + dr, c + dc  
                perimeter += dfs(rr, cc)
            return perimeter

        
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    return dfs(r, c)
        return 0 



        