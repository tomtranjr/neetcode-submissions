class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = collections.deque() # tracks the indexes of elements in nums
        l = r = 0

        while r < len(nums):
            # clear previous values in q that are less than current value at r
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            
            # append index of current element
            q.append(r)

            # check if we are out of bounds
            # l tracks left bound of window, so if greater than index in q we popleft
            if l > q[0]:
                q.popleft()
            
            # now if window is valid, we append current value of q to res
            # increment l to keep window size fixed
            if (r + 1) >= k:
                res.append(nums[q[0]])
                l += 1
            r += 1
            
        return res