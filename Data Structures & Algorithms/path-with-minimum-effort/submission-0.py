class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        DIRs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        ROW, COL = len(heights), len(heights[0])
        
        heap = [(0, (0, 0))]
        dist = [[float('inf') for _ in range(COL)] for _ in range(ROW)]
        dist[0][0] = 0

        visited = set()

        while heap:
            cur_d, (x, y) = heapq.heappop(heap)
            if cur_d > dist[x][y]:
                continue
 
            if x == ROW-1 and y == COL-1:
                return cur_d
      
            for dr, dc in DIRs:
                r, c = x + dr, y + dc
                if 0 <= r < ROW and 0<= c < COL:
                    absdiff = abs(heights[r][c] - heights[x][y])
                    new_d = max(cur_d, absdiff)
                    if new_d < dist[r][c]:
                        dist[r][c] = new_d
                        heapq.heappush(heap, (dist[r][c], (r, c)))
        return 0