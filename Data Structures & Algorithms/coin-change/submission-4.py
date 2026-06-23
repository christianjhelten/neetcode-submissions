class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # Store a value larger than any possible coin count

        impossible = amount + 1

        # dp[x] means minimum coins needed to make amount x

        dp = [impossible] * (amount + 1)

        # Amount 0 needs 0 coins

        dp[0] = 0

        # Build answers for every amount up to target

        for current_amount in range(1, amount + 1):

            # Try making current_amount by using each coin last

            for coin in coins:

                # Skip coins that are too large

                if coin > current_amount:

                    continue

                # Use this coin plus best way to make the remaining amount

                dp[current_amount] = min(dp[current_amount], 1 + dp[current_amount - coin])

        # If target stayed impossible, no combination works

        if dp[amount] == impossible:

            return -1

        # Otherwise return the fewest coins for target

        return dp[amount]