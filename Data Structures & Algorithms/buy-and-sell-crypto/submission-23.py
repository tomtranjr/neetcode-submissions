class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0

        l = 0
        for r in range(len(prices)):
            currProfit = prices[r] - prices[l]
            if currProfit > 0:
                maxP = max(maxP, currProfit)
            else:
                l = r
            
        
        return maxP