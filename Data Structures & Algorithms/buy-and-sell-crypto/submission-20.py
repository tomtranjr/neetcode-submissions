class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # brute force
        # -----------
        # res = 0
        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         profit = prices[j] - prices[i]
        #         res = max(res, profit)
        # return res

        # sliding window
        # --------------
        res = 0
        l = 0
        for r in range(len(prices)):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                res = max(res, profit)
            else:
                l = r
        return res