class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 1. init indegree, and adj
        courses = set()
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        # course -> prereq
        for course, prereq in prerequisites:
            adj[course].append(prereq)
            indegree[prereq] += 1
            courses.add(course)
            courses.add(prereq)

        # print(indegree)
        # print(adj)

        # 2. add ingreee 0 to queue
        queue = deque([c for c in range(numCourses) if indegree[c] == 0])
        print(queue)


        # 3. bfs
        taken_reversed = []
        while queue:
            pop = queue.popleft()
            taken_reversed.append(pop)
            for dep in adj[pop]:
                indegree[dep] -= 1
                if indegree[dep] == 0:
                    queue.append(dep)

        # 4. check cycles
        print(taken_reversed)
        taken = taken_reversed[::-1]
        print(taken)
        return taken if len(taken) == numCourses else []
        