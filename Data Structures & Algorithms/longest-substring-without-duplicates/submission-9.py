class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # brute force
        # res = 0

        # for i in range(len(s)):
        #     charSet = set()
        #     for j in range(i, len(s)):
        #         if s[j] in charSet:
        #             break
        #         charSet.add(s[j])
        #     res = max(res, len(charSet))
    
        # return res

        # sliding window
        # init res, window (hashSet), l at 0
        # iter through r:
        # while elem at r in set, remove and incr l
        # add elem at r to window
        # last, update res and return res
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
