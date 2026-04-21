class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        tickets = tickets[::-1]
        adj = defaultdict(list)
        for src, tgt in tickets:
            adj[src].append(tgt)
        
        res = []
        
        def dfs(node):
            nonlocal res
            while adj[node]:
                tgt = adj[node].pop()
                dfs(tgt)
            res.append(node)
        dfs('JFK')
        return res[::-1]

        # ans = ['JFK']
        # def dfs(node):
        #     nonlocal ans
        #     if len(ans) == len(tickets) + 1:
        #         return True
        #     # prune
        #     if node not in adj:
        #         return False
        #     # explore
        #     for i, nei in enumerate(adj[node]):
        #         # choose
        #         adj[node].pop(i)
        #         ans.append(nei)
        #         # repeat
        #         if dfs(nei):
        #             return True
        #         # backtrack
        #         adj[node].insert(i, nei)
        #         ans.pop()
        #     return False
               
        # dfs('JFK')
        # return ans
        