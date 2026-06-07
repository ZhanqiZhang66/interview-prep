class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        # dp[i]: the difference between cur player and opponent, at stone i, for action take 1 take 2 and take 3
        # which is how much cur player gain with the action - how much cur player has gain at the next state
        n = len(stoneValue)
        dp = [float('-inf')] * (n + 1)
        dp[n] = 0

        for i in range(n - 1, -1 , -1):
            taken = 0
            for j in range(3):
                if i + j < n:
                    taken += stoneValue[i + j]
                    dp[i] = max(dp[i], taken - dp[i + j + 1])
        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"


        