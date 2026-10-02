class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        tmp = []
        for num, cnt in counter.items():
            tmp.append((cnt, num))
        tmp.sort()

        res = []
        while len(res) < k:
            res.append(tmp.pop()[-1])

        return res