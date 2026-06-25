class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_nums = Counter(nums)
        output = list(item[0] for item in sorted(count_nums.items(), key=lambda item: item[1], reverse=True))
        return output[:k]