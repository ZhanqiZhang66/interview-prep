class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        DIRS = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        minHeap = [(grid[0][0], [0, 0])]
        dist = [[float('inf') for _ in range(n)] for _ in range(n)]
        dist[0][0] = grid[0][0]

        while minHeap:
            d, [i, j] = heapq.heappop(minHeap)
            print(f"{d} ,[{i},{j}] {grid[i][j]}")
            if i == n- 1 and j == n - 1:
                return dist[n - 1][n - 1]
            if d > dist[i][j]:
                continue
            
            for dr, dc in DIRS:
                r = i + dr
                c = j + dc
                if r in range(n) and c in range(n):
                    max_height = max(d, grid[r][c])
                    if max_height < dist[r][c]:
                        dist[r][c] = max_height
                        print(f"update dist {dist} at {r},{c} btw{d}, {grid[r][c]}")
                        heapq.heappush(minHeap, (max_height, (r, c)))
        print(dist)
        return dist[n - 1][n - 1]
      