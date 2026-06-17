class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[a] = fewest coins needed to make exact amount a
        # INF means amount a is not reachable yet
        INF = float('inf')
        dp = [INF] * (amount + 1)
        dp[0] = 0

        # Build answers from smaller amounts to larger amounts
        for current_amount in range(1, amount + 1):
            for coin in coins:
                previous_amount = current_amount - coin
                if previous_amount >= 0 and dp[previous_amount] != INF:
                    dp[current_amount] = min(
                        dp[current_amount],
                        dp[previous_amount] + 1
                    )

        return -1 if dp[amount] == INF else dp[amount]