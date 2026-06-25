class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i,j]
        
        return []

    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     l, r = 0, len(nums) - 1
    #     while l < r:
    #         if nums[l] + nums[r] == target:
    #             return [l, r]
    #         elif nums[l] + nums[r] > target:
    #             r -= 1
    #         else:
    #             l += 1
    #     return []