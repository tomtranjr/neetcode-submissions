class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # brute force
        # res = []

        # for i in range(len(nums) - k + 1):
        #     maxi = nums[i]
        #     for j in range(i, i + k):
        #         maxi = max(maxi, nums[j])
        #     res.append(maxi)
        # return res

        # deque
        res = []
        q = collections.deque()
        l = r = 0

        while r < len(nums):
            # pop smaller values from q
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                res.append(nums[q[0]])
                l += 1
            r += 1

        return res