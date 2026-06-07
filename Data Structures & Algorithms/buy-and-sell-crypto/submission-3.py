class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        win = []
        win.append(0)
        for i in range(len(prices)-1):
            if prices[i] < max(prices[i+1:]):
                win.append(max(prices[i+1:]) - prices[i])
        
        return max(win)