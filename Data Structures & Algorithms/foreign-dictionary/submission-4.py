class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        # topo sort
        # 1. init indegree and adj
        import string
        indegrees = {char: 0 for w in words for char in w}
        adj = {char: [] for w in words for char in w}
     

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            min_len = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
            for j in range(min_len):
                c1, c2 = w1[j], w2[j]
                if c1 == c2:
                    continue
                else:
                    # c1 -> c2
                    if c2 not in adj[c1]:
                        adj[c1].append(c2)
                        indegrees[c2] += 1
                    break
        print(adj)
        print(indegrees)
        # 2.  init queue with nodes indegree == 0
        q = deque([char for char in indegrees if indegrees[char] == 0])

        # 3. BFS
        res = []
        while q:
            pop = q.popleft()
            res.append(pop)
            
            for nei in adj[pop]:
                print(f"added {res}, nei = {nei}")
                indegrees[nei] -= 1
                print(f"nei's deg = {indegrees[nei]}")
                if indegrees[nei] == 0:
                   
                    q.append(nei)
                    print(f"{nei}'s deg - .q:{q}")

        # 4 check cycles
        return "".join(res) if len(res) == len(indegrees) else ""
        
        
        