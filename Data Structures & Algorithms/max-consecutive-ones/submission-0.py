class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        best = 0
        curr_best = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                curr_best += 1
            else:
                best = max(best, curr_best)
                curr_best = 0
        return max(best, curr_best)
