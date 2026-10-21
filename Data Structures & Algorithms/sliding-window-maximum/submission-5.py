class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = collections.deque() # store indexes for elements in nums
        l = r = 0

        while r < len(nums):
            # pop values from q less than current value
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            # once all lower values popped, we append r
            q.append(r)
        
            # if l is greater than index at front of queue, we leftpop
            if l > q[0]:
                q.popleft()
            
            # if the window is valid, then we append the element at front of q
            if (r + 1) >= k:
                res.append(nums[q[0]])
                l += 1
            r += 1
        
        return res