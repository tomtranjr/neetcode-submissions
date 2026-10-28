class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # brute force
        for i, num in enumerate(nums):
            if num == target:
                return i
        return -1