class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        DIR = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        ROW = len(grid)
        COL = len(grid[0])

        ans = 0
        queue = deque()
        fresh = 0

        # put all rotten into queue,
        for r in range(ROW):
            for c in range(COL):
                print(r)
                print(c)
                if grid[r][c] == 2:
                    queue.append((r, c))
                if grid[r][c] == 1:
                    fresh += 1   
        # run multi-source bfs while have fresh
        while fresh > 0 and queue:
            print(f"time = {ans} with q={len(queue)} and {fresh} remains")
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in DIR:
                    if (r+dr) in range(ROW) \
                        and (c+dc) in range(COL) \
                        and grid[r + dr][c + dc] == 1:
                        grid[r + dr][c + dc] = 2
                        fresh -= 1
                        queue.append((r+ dr, c+ dc))
            ans += 1
        
        return ans if fresh == 0 else -1

        