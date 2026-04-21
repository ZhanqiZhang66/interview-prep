class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp =[[float('-inf')] * (n+1) for _ in range(n+1)]
        dp[n][n] = 1
        max_p = nums[-1]
        for i in range(n-1, -1 , -1):
            for j in range(i, n+1):  
                if j == i:
                    dp[i][j] = nums[i]
                else:
                    print(f"i={i}, j={j} nums[i] = {nums[i]}, dp = max({nums[i] * dp[i+1][j]} ,{nums[i]}")
                    dp[i][j] = max(nums[i] * dp[i+1][j], nums[i])
                    print(f"dp[{i}][{j}] = {dp[i][j] }")
                
                max_p = max(max_p, dp[i][j])
        print(dp)
        return max_p
        