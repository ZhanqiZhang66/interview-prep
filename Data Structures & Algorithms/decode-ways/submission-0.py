class Solution:
    def numDecodings(self, s: str) -> int:
        
        n = len(s)
        dp = {n: 1}


        for i in range(n-1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                # 1 step 
                dp[i] = dp[i+1]
            # 2 steps
    
            if i+ 1 < n and (s[i] == "2" and int(s[i+1]) <= 6) or (s[i]== "1"):
                print(f"i={i}, {s[i]} {s[i+1]} move 2")
                dp[i] += dp[i+2] 
        return dp[0]

            
        