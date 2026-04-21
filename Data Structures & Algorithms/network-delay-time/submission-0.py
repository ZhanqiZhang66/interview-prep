class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n+1)]
        
        for u, v, w in times:
            adj[u].append((v, w))

        # create (dist, node) pair
        # add start 
        dist = [float('inf')] * (n+1)
        dist[k] = 0
        visited = set()
        minHeap = [(0, k)]

        while minHeap:
            # 1. get shortest path to node u
            d, u = heapq.heappop(minHeap)
            visited.add(u)
            if d > dist[u]:
                continue
            for v, w in adj[u]:
                if not v in visited:
                    if dist[v] > w + d:
                        dist[v] = w + d
                        heapq.heappush(minHeap, (dist[v], v))
        if float('inf') in dist[1:]:
            return -1
        return max(dist[1:])



        

        