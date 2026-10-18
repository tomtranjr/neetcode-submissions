class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # brute force
        # res = 0
        # for i, char in enumerate(s):
        #     charSet = set()
        #     for j in range(i, len(s)):
        #         if s[j] in charSet:
        #             break
        #         charSet.add(s[j])
        #     res = max(res, len(charSet))
        # return res

        # sliding window
        window = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l])
                l += 1
            window.add(s[r])
            res = max(res, r - l + 1)
        return res

