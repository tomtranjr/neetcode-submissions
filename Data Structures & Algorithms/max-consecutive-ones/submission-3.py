class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        best = 0
        curr = 0
        for num in nums:
            if num == 1:
                curr += 1
            else:
                curr = 0
            best = max(best, curr)
        return best
