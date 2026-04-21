class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        min_p = float('inf')
        max_profit = 0
        for price in prices:
            min_p = min(price, min_p)
            max_profit = max(price - min_p, max_profit)
   
        return max_profit


        