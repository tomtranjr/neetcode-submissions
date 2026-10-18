class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the input array
        # iter thru the array for ea num
        # if elem > 0, we can break bc no way to sum to 0
        # if elem is same as prev elem, we can continue, no dups
        # init l and r pointer for rest of array
        # if threeSum > 0: decr r pointer
        # if threeSum < 0: incr l pointer
        # else: res.append([elem, elem l, elem r])
        # incr l, decr r
        # ensure l is not at a duplicate and l < r, l += 1

        res = []
        nums.sort()

        for idx, num in enumerate(nums):
            if num > 0:
                break

            if idx > 0 and num == nums[idx - 1]:
                continue

            l = idx + 1
            r = len(nums) - 1

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