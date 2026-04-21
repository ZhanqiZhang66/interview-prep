class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # dijkstra stop when k == k return res[cur], else return -1

        # 1. build adj
        adj = defaultdict(list)
        for from_f, to_f, price in flights:
            adj[from_f].append((to_f, price))

        # 2. dist, minHeap((dist, node))
        dist = [[float('inf')] * (k+2) for _ in range(n)]
        print(dist)
        dist[src][0] = 0
        #    -1 0 2 3 ..
        # n1. 0
        minHeap = [(0, 0, src)]

        # 3. heap
        while minHeap:
            d, transit, node = heapq.heappop(minHeap)
            if node == dst:
                return d
            if transit == k+1 or d > dist[node][transit]:
                continue      
            for nei, price in adj[node]:
                nei_dist = d + price
                if nei_dist < dist[nei][transit+1]:
                    dist[nei][transit+1] = nei_dist       
                    heapq.heappush(minHeap, (dist[nei][transit+1], transit+1, nei))
        return -1


        