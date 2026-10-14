class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # two pointer technique
        # init left and right pointer
        # take advantage of sorted nondec order
        # compute current sum at l and r pointer
        # if current sum less than target: need to inc curr sum => l += 1
        # if current sum greater than target: need to dec curr sum => r -= 1
        # return [l+1, r+1]
        l, r = 0, len(numbers) - 1
        while l < r:
            currSum = numbers[l] + numbers[r]
            if currSum < target:
                l += 1
            elif currSum > target:
                r -= 1
            else:
                return [l + 1, r + 1]