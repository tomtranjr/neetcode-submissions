class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # res = 0
        # currSum = sum(arr[:k - 1])

        # for L in range(len(arr) - k + 1):
        #     currSum += arr[L + k - 1]
        #     if (currSum / k) >= threshold:
        #         res += 1
        #     currSum -= arr[L]
        # return res

        # optimized by getting threshold * k = target

        res = 0
        target = threshold * k
        currSum = sum(arr[:k - 1])

        for L in range(len(arr) - k + 1):
            currSum += arr[L + k - 1]
            if currSum >= target:
                res += 1
            currSum -= arr[L]
        return res