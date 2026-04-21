class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        adj = {src: [] for src, tgt in tickets}
        for src, tgt in tickets:
            adj[src].append(tgt)

        ans = ['JFK']
        def dfs(node):
            nonlocal ans
            if len(ans) == len(tickets) + 1:
                return True
            if node not in adj:
                return False

            for i, nei in enumerate(adj[node]):
                adj[node].pop(i)
                ans.append(nei)
                if dfs(nei):
                    return True
                adj[node].insert(i, nei)
                ans.pop()
            return False
               
        dfs('JFK')
        return ans
        