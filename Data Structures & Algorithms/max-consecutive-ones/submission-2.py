class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        best = 0
        curr_best = 0
        for num in nums:
            if num == 1:
                curr_best += 1
            else:
                best = max(best, curr_best)
                curr_best = 0
        return max(best, curr_best)