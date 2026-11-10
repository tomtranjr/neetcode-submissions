class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0

        l = 0
        for r in range(len(prices)):
            currProfit = prices[r] - prices[l]
            if currProfit < 0:
                l = r
            maxProfit = max(maxProfit, currProfit)
        
        return maxProfit