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
        if fresh == 0:
            return 0
        
        # run multi-source bfs
        print(fresh)
        while queue:
            print(f"time = {ans} with q={len(queue)} and {fresh} remains")
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in DIR:
                    if 0 <= r+ dr <= ROW -1 \
                        and 0<= c+dc <= COL -1 \
                        and grid[r + dr][c + dc] == 1:
                        grid[r + dr][c + dc] = 2
                        fresh -= 1
                        queue.append((r+ dr, c+ dc))
            ans += 1
        
        return ans-1 if fresh == 0 else -1

        