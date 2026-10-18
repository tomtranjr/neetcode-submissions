class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # # brute force approach
        # # init res = 0
        # # double for loop calculating max profit until end of array
        # res = 0
        # for idx, price in enumerate(prices):
        #     for j in range(idx + 1, len(prices)):
        #         profit = prices[j] - prices[idx]
        #         res = max(res, profit)
        # return res
        # T: O(n^2)
        # S: O(1)

        # sliding window approach
        res = 0
        l, r = 0, 1

        while r < len(prices):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                res = max(res, profit)
            else:
                l = r
            r += 1

        return res
        # T: O(n)
        # S: O(1)
