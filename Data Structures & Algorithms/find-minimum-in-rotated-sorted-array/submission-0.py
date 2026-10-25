class Solution:
    def findMin(self, nums: List[int]) -> int:
        # brute force
        mini = float("inf")

        for num in nums:
            if num < mini:
                mini = num
        return mini