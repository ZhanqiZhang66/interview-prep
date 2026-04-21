class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        DIRS = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        minHeap = [(0, [0, 0])]
        dist = [[float('inf') for _ in range(n)] for _ in range(n)]
        dist[0][0] = 0

        while minHeap:
            d, [i, j] = heapq.heappop(minHeap)
            print(f"{d} ,[{i},{j}] {grid[i][j]}")
            if d > dist[i][j]:
                continue
            
            for dr, dc in DIRS:
                r = i + dr
                c = j + dc
                if r in range(n) and c in range(n):
                    if grid[r][c] > grid[i][j]:
                        w = grid[r][c] - grid[i][j]
                        print(f"{r},{c}")
                        print(f"{grid[i][j]}-{grid[r][c]} = {w}")
                    else:
                        w = 0
                        print(f"{w}")
                    print(f"{d} + {w} vs {dist[r][c]}")
                    if dist[r][c] > d + w:
                        dist[r][c] = d + w
                        print(f"update dist {dist} at {r},{c}")
                        heapq.heappush(minHeap, (dist[r][c], (r, c)))
        print(dist)
        return dist[n - 1][n - 1]



        