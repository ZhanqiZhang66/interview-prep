class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        min_buy = prices[0]
        max_profit = 0
        for price in prices:
            min_buy = min(price, min_buy)
            max_profit = max(price - min_buy, max_profit)
   
        return max_profit


        