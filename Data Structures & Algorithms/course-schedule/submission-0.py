class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 1. build adj, indegree
        # c -> prereq
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for c, prereq in prerequisites:
            adj[c].append(prereq)
            indegree[prereq] += 1

        # 2. init queue with indegree 0
        queue = deque([c for c in range(numCourses) if indegree[c] == 0])

        # 3. bfs
        taken = 0
        while queue:
            pop = queue.popleft()
            taken += 1
            if len(adj[pop]):
                for adj_c in adj[pop]:
                    indegree[adj_c] -= 1
                    if indegree[adj_c] == 0:
                        queue.append(adj_c)
        # 4. check cycles
        return taken == numCourses  
        