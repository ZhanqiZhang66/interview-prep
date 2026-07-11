class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = [[] for _ in range(numCourses)]
        indegrees = [0] * numCourses
        isprereq = defaultdict(set)
        for u, v in prerequisites:
            adj[u].append(v)
            indegrees[v] += 1
        
        q = deque([u for u in range(numCourses) if indegrees[u] == 0])
       
        while q:
            node = q.popleft()
            for nei in adj[node]:
                isprereq[nei].add(node)
                isprereq[nei].update(isprereq[node])
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    q.append(nei)
        return [u in isprereq[v] for u, v in queries]
