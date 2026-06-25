class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for idx, num in enumerate(nums):
            needed = target - num
            if needed in hash_map:
                return [hash_map[needed], idx]
            hash_map[num] = idx
        
        return [-1,-1]