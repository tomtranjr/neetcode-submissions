class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create a counter of the elements
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        # create an intermediate arr that stores [count, num], then sort
        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort()

        # create result arr that is appended by popping from sorted arr
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
