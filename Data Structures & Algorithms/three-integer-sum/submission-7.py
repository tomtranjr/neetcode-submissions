class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for idx, num in enumerate(nums):
            # since sorted, next nums after num are > 0 => cannot sum to zero
            if num > 0:
                break
            
            # check that curr num is not same as prev num
            if idx > 0 and num == nums[idx - 1]:
                continue
            
            l, r = idx + 1, len(nums) - 1
            while l < r:
                threeSum = num + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return res

