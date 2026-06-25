class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # brute force double for loop
        n = len(nums)

        output = []
        for i in range(n):
            total = 1
            for j in range(n):
                if i != j:
                    total *= nums[j]
            output.append(total)
        return output