class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # create a hashset for look up
        # initialize res = 0
        # check that its beginning of seq (that n-1 not in hashset)
        # if yes, set length = 1
        # while num + length in hashset:
        # length += 1
        # update res to max between res and length
        # return res

        hashset = set(nums)
        res = 0

        for num in nums:
            if (num - 1) not in hashset:
                length = 1
                while num + length in hashset:
                    length += 1
                res = max(res, length)
        return res