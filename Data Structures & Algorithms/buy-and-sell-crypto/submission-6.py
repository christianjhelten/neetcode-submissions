class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = []
        profit.append(0)

        for i in range(len(prices)):
            if prices[i] < max(prices[i:]):
                profit.append(max(prices[i:]) - prices[i])

        return max(profit)

            
