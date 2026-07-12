class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        n = len(equations)
        adj = defaultdict(list)
        for i in range(len(equations)):
            x, y = equations[i]
            val = values[i]
            adj[x].append((y, val))
            adj[y].append((x, 1 / val))

        res = []
        

        def dfs(query, visited):
   
            if query[0] not in adj or query[1] not in adj:
                return -1
            if query[0] == query[1]:
                return 1
            visited.add(query[0])
            for nei, val in adj[query[0]]:
                if nei not in visited:
                    v = dfs([nei, query[1]], visited)
                    if v != -1:
                        return v * val
            return -1

            
        for query in queries:
            res.append(dfs(query, set()))
        return res

        