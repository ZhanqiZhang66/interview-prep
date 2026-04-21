class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        DIRS = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        minHeap = [(grid[0][0], [0, 0])]
        height = [[float('inf') for _ in range(n)] for _ in range(n)]
        height[0][0] = grid[0][0]

        while minHeap:
            h, [i, j] = heapq.heappop(minHeap)
            print(f"{h} ,[{i},{j}] {grid[i][j]}")
            if i == n- 1 and j == n - 1:
                return height[n - 1][n - 1]
            if h > height[i][j]:
                continue
            
            for dr, dc in DIRS:
                r = i + dr
                c = j + dc
                if r in range(n) and c in range(n):
                    if h > grid[r][c]:
                        curr_height = h
                    else:
                        curr_height = grid[r][c]
                    # max_height = max(d, grid[r][c])
                    if curr_height < height[r][c]:
                        height[r][c] = curr_height
                        print(f"update dist {height} at {r},{c} btw{h}, {grid[r][c]}")
                        heapq.heappush(minHeap, (curr_height, (r, c)))
        print(height)
        return height[n - 1][n - 1]
      