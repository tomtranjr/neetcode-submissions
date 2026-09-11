class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create a counter of elements
        counter = Counter(nums)

        # create a tmp array with (count, num) pairs, then sort
        tmp = []
        for num, count in counter.items():
            tmp.append((count, num))
        tmp.sort()

        # create result array and pop until desired k
        res = []
        while len(res) < k:
            res.append(tmp.pop()[1])
        
        return res