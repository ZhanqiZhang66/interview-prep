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
            # prune
            if node not in adj:
                return False
            # explore
            for i, nei in enumerate(adj[node]):
                # choose
                adj[node].pop(i)
                ans.append(nei)
                # repeat
                if dfs(nei):
                    return True
                # backtrack
                adj[node].insert(i, nei)
                ans.pop()
            return False
               
        dfs('JFK')
        return ans
        