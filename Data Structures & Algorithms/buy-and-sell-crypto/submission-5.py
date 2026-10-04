class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # brute force: check every possible pair
        # max_profit = 0
        # for i in range(len(prices)):
        #     for j in range(i + 1, len(prices)):
        #         curr_profit = prices[j] - prices[i]
        #         max_profit = max(max_profit, curr_profit)
        # return max_profit

        # two pointer
        l, r = 0, 1 # l is buy day, r is sell day
        max_profit = 0

        while r < len(prices):
            if prices[r] > prices[l]:
                max_profit = max(max_profit, prices[r] - prices[l])
            else:
                l = r
            r += 1
        return max_profit





