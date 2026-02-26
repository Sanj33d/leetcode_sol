class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # bottom up -> dp : from dp[0],dp[1],...dp[amount]
        # top down -> memoization : from amount, amount - each_coin...., 0

        # dp approach
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for amt in range(1, amount + 1):
            for coin in coins:
                if amt - coin >= 0:
                    dp[amt] = min(dp[amt], 1 + dp[amt-coin])
        
        if dp[amount] != amount + 1:
            return dp[amount]
        else:
            return -1
            
        