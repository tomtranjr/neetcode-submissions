class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # while l < r:
        # curr_sum = element at left pointer + element at right pointer
        # if curr_sum == target: return [l+1, r+1]
        # if curr_sum < target: increment left pointer
        # if curr_sum > target: decrement right pointer

        l, r = 0, len(numbers) - 1
        while l < r:
            curr_sum = numbers[l] + numbers[r]
            if curr_sum == target:
                return [l+1, r+1]
            elif curr_sum < target:
                l += 1
            elif curr_sum > target:
                r -= 1
