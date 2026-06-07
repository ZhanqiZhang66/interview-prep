class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1) # how many ways can amount be made
        dp[0] = 1

        
        for a in range(target+1):
            for n in nums:
                if a >= n:
                    dp[a] = dp[a] + dp[a - n] 
        return dp[-1]
        