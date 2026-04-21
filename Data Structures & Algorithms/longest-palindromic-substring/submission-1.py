class Solution:
    def longestPalindrome(self, s: str) -> str:
        resI, resL = 0, 0
        n = len(s)
        dp = [[False] *  n for _ in range(n)]

        # [          i]
        # [    i . . .]
        # [    i j j j]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                # Outer must match &&  Inner must match (<=3 and >=4)
                if s[i] == s[j]    and ((j - i <=2) or dp[i+1][j-1]):
                    dp[i][j] = True
                    if j - i + 1 > resL:
                        resI = i
                        resL = j - i + 1

        return s[resI: resI+resL]

        