class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indegree = defaultdict(int)
        outdegree = defaultdict(int)
        for u, v in trust:
            indegree[v] += 1
            outdegree[u] += 1
        for v in range(1, n + 1):
            if indegree[v] == n - 1 and outdegree[v] == 0:
                return v
        return -1
        