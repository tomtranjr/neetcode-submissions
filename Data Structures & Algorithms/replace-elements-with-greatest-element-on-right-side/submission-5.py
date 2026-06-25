class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans = [0] * n
        right_max = -1

        for idx in range(n-1, -1, -1):
            ans[idx] = right_max
            right_max = max(right_max, arr[idx])

        return ans