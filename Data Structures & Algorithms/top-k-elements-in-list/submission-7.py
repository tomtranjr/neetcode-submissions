class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create a count of the input array
        count = Counter(nums)
        # create an intermediate array with count, element then sort
        arr = []
        for num, freq in count.items():
            arr.append([freq, num])
        arr.sort()
        # create and return result array by popping from intermediate array
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
