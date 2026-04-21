class Solution:
    def climbStairs(self, n: int) -> int:
        # memo = {}
        # def dp(state):
        #     if state == n or state == (n - 1):
        #         return 1
        #     if state > n:
        #         return 0
            
        #     if state in memo:
        #         return memo[state]
        #     memo[state] = dp(state + 1) + dp(state + 2)
        #     return memo[state]

        # return dp(0)
        if n == 1:
            return 1
        s = [-1] * n
        s[0] = 1
        s[1] = 2

        for i in range(2, n):
            s[i] = s[i-1] + s[i-2]
        return s[n-1]
        