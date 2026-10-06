class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # brute force O(n^2)

        # hash map, key: element and value: index
        # create a hashmap seen
        # search for diff = target - curr_elem 
        # if diff in hashmap: return hashmap index, current index
        # else: add element, index to our hashmap
        seen = dict()

        for idx, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], idx]
            else:
                seen[num] = idx
