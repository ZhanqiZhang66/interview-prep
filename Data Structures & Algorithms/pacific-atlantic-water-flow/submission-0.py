class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, alt = set(), set()

        def dfs(r, c, preHeight, visited):
            if (r not in range(ROWS) or \
            c not in range(COLS) or heights[r][c] < preHeight or \
            (r, c) in visited):

                return
            visited.add((r, c))
            dfs(r + 1, c, heights[r][c], visited)
            dfs(r - 1, c, heights[r][c], visited)
            dfs(r, c + 1, heights[r][c], visited)
            dfs(r, c - 1, heights[r][c], visited)


        # start from each boarder,  go inward recursively
        for c in range(COLS):
            dfs(0, c, heights[0][c], pac)
            dfs(ROWS - 1, c, heights[ROWS-1][c], alt)
        for r in range(ROWS):
            dfs(r, 0, heights[r][0], pac)
            dfs(r, COLS -1, heights[r][COLS - 1], alt)


        # find intersect of pac and alt

        return list(alt.intersection(pac)) 
        