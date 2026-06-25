class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i,j]
        
        return []

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l] + nums[r] == target:
                return [l, r]
            elif nums[l] + nums[r] > target:
                r -= 1
            else:
                l += 1
        return []

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for index, num in enumerate(nums):
            needed = target - num
            if needed in hash_map:
                return [hash_map[needed], index]
            else:
                hash_map[num] = index
        
        return [-1,-1]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for index, num in enumerate(nums):
            needed = target - nums[index]
            if needed in hash_map:
                return [hash_map[needed], index]
            else:
                hash_map[num] = index





