class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Use Dynamic Programming
        
        # Array to store the min. num of coins for each amount
        dp = [float('inf')] * (amount + 1)
        
        # Base case
        # 0 needed for amount 0
        dp[0] = 0
        
        # Iterate through coin denomincations update the dp array
        for coin in coins:
            for i in range(coin, amount + 1):
                # Represents the minimum number of coins needed to make up the amount 'i', using current coin denomination
                dp[i] = min(dp[i],dp[i-coin]+1)
        print(dp)
        
        # Check if it's possible to make up the given amount
        return dp[amount] if dp[amount] != float('inf') else -1
    
    # T.C: O(N*amount), no.of coins, nested loop through all amounts up to target amount
    # S.C: O(amount)