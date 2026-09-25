class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        res = 0

        for num in nums:
            longest = 1
            if (num - 1) not in num_set:
                while (num + longest) in num_set:
                    longest += 1
            res = max(res, longest)
    
        return res