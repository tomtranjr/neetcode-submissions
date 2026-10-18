class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window approach
        # use left and right pointer
        # window as hash set
        # for each right pointer:
        # while element at right pointer in window:
        # remove element at left, increment left pointer
        # add the right most element to window
        # update res as max btwn res and curr window length (r - l + 1)
        window = set()
        res = 0
        l = 0

        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l])
                l += 1
            window.add(s[r])
            res = max(res, r - l + 1)
        return res