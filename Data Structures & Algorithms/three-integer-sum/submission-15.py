class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for idx, num in enumerate(nums):
            # since array sorted, if curr elem > 0, next elems > 0 => sum != 0
            if num > 0:
                break
            
            # since array can contain duplicates, ensure curr elem is not same as prev elem
            if idx > 0 and num == nums[idx - 1]:
                continue
            
            # perform two pointer on rest of array, after curr elem
            l, r = idx + 1, len(nums) - 1
            while l < r:
                threeSum = num + nums[l] + nums[r]
                if threeSum < 0:
                    l += 1
                elif threeSum > 0:
                    r -= 1
                else:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    # while l < r and nums[r] == nums[r - 1]:
                    #     r -= 1
        return res