class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                # The price is increasing , so we should buy on the previous day and sell on this day to make a profit
                profit += prices[i] - prices[i-1]
                
        return profit