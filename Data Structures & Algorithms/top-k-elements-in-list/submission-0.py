class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # simple base cases
        # 1. empty array
        # 2. length of array is 1
        length = len(nums)
        if length == 0 or length == 1:
            return nums
        
        hashmap = {}

        for num in nums:
            if num in hashmap.keys():
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        
        freq = sorted([x for x in hashmap.values()], reverse=True)
        freq = freq[:k]

        result = []
        for key, value in hashmap.items():
            if value in freq:
                result.append(key)
        
        return result