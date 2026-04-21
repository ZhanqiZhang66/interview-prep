class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # dijkstra stop when k == k return res[cur], else return -1

        # 1. build adj
        adj = defaultdict(list)
        for from_f, to_f, price in flights:
            adj[from_f].append((to_f, price))

        # 2. dist, minHeap((dist, node))
        dist = [float('inf')] * n
        dist[src] = 0
        minHeap = [(0, 0, src)]
        visited = set()
        # 3. heap

        i = 0
        while minHeap and i < k+2:
            print(minHeap)
            num_transit, d, node = heapq.heappop(minHeap)
   
            i += 1
            print(f"i={i}")
            visited.add(node)  
            print(f"visited {node}, {d}")     
            
            if d < dist[node]:
                continue
            
            for nei, price in adj[node]:
                nei_dist = d + price
                if nei == dst:
                    return min(nei_dist, dist[nei])
                if nei_dist < dist[nei]:
                    dist[nei] = nei_dist
                   
                    heapq.heappush(minHeap, (num_transit+1, dist[nei], nei))
         
              
     
        return -1


        