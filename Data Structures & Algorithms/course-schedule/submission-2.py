class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        indegrees = [0] * numCourses
        for a, b in prerequisites:
            adj[a].append(b)
            indegrees[b] += 1

        visited = set()
        q = deque([course for course in range(numCourses) if indegrees[course] == 0])

        while q:
            course = q.popleft()
            visited.add(course)

            for nei in adj[course]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    q.append(nei)
        return len(visited) == numCourses
        
        
        
        