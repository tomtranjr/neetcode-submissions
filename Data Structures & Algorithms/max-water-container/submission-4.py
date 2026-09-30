class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # # brute force:
        # # interate through heights calculate area
        # # compare best with curr_area, take max
        # # return best
        # # O(n^2)
        # best = 0
        # for i in range(len(heights)):
        #     for j in range(i + 1, len(heights)):
        #         best = max(best, min(heights[i], heights[j]) * (j-i))
        # return best
        l, r = 0, len(heights) - 1
        res = 0
        
        while l < r:
            curr_area = min(heights[l], heights[r]) * (r - l)
            res = max(res, curr_area)
            if heights[l] <= heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
        
        return res