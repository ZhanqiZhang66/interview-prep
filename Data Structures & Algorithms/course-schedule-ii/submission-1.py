class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        indegrees = [0] * numCourses
        for a, b in prerequisites:
            adj[a].append(b)
            indegrees[b] += 1

        to_take = []
        q = [course for course in range(numCourses) if indegrees[course] == 0]

        while q:
            course = q.pop()
            to_take.append(course)
            for nei in adj[course]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    q.append(nei)
        return to_take[::-1] if len(to_take) == numCourses else []
        