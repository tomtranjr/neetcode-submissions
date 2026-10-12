class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            # need to break since sorted so every element after is positive
            if a > 0:
                break
            
            # if same element as prev, move onto the next one
            if i > 0 and a == nums[i - 1]:
                continue
            
            # two pointer for rest of the array after element a
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    # add result, then step both pointers
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # if same element, increment l
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res

