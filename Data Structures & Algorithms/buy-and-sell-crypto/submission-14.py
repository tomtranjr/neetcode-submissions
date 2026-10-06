class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # use two pointers l at 0 and r at 1
        # set a max profit = 0
        # while r in bound of prices
        # if price[r] > price[l]:
        # update max price to max between max price and price[r] - price[l]
        # else: set l to r
        # always increment r += 1
        l, r = 0, 1
        maxProfit = 0

        while r < len(prices):
            if prices[r] > prices[l]:
                maxProfit = max(maxProfit, prices[r] - prices[l])
            else:
                l = r
            r += 1
        
        return maxProfit