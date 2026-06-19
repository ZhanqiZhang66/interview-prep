class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [[float('inf') for _ in range(k + 1)] for _ in range(n + 1)]  #largest sum of subarray :i if cut k time
        dp[0][0] = 0
        p = 0
        prefix = [0]
        for num in nums:
            p += num
            prefix.append(p)
        

        for i in range(1, n + 1):
            for c in range(1, k + 1):
                for j in range(c - 1, i):
                    dp[i][c] = min(
                        max(dp[j][c-1], prefix[i] - prefix[j]), 
                        dp[i][c])
        print(dp)
        return dp[n][k]


        
            

        