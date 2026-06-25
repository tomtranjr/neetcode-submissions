class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # create a list
        seen = []
        # check if the number is in the list
        for num in nums:
        # if yes return True
            if num in seen:
                return True
            else:
        # if no, append and keep going
                seen.append(num)
        return False