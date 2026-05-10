class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1, text2 = text2, text1
        m = len(text1)
        n = len(text2)
        prev = [0 for _ in range(n + 1)]    
        curr = [0 for _ in range(n + 1)] 

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1): 
                if text1[i] == text2[j]:
                    curr[j] = 1 + prev[j+1]
                else:
                    curr[j] = max(prev[j], curr[j+1])
            tmp = prev
            prev = curr
            curr = tmp
        return prev[0]
        

        # m = len(text1)
        # n = len(text2)
        # dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    
        
        # for i in range(m-1, -1, -1):
        #     for j in range(n-1, -1, -1):
        #         # i and j same
        #         if text1[i] == text2[j]:
        #             dp[i][j] = 1 + dp[i+1][j+1]
        #         else:
        #         # i and j not same
        #             dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        # return dp[0][0]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # n = len(text1) 
        # m = len(text2) 

        # dp = [[0] * (m+1) for _ in range(n+1)] # n x m

        # for i in range(n-1, -1, -1):
        #     for j in range(m-1, -1, -1):
        #         if text1[i] == text2[j]:
        #             dp[i][j] = 1 + dp[i+1][j+1]
        #         else:
        #             dp[i][j] = max(dp[i][j+1], dp[i+1][j])
        # return dp[0][0]