class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        minCost = [0] * (len(cost) + 1)

        for i in range(2, len(cost)+1):
            minCost[i] = min(cost[i-2]+minCost[i - 2], cost[i-1]+minCost[i-1])
        print(minCost)
        return minCost[len(cost)]