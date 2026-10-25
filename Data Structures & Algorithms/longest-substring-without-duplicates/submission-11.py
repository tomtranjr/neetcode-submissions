class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # brute force
        # res = 0
        # for i in range(len(s)):
        #     window = set()
        #     for j in range(i, len(s)):
        #         if s[j] not in window:
        #             window.add(s[j])
        #         else:
        #             res = max(res, len(window))
        #             break
        # return res

        # sliding window
        l = 0
        window = set()
        res = 0

        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l])
                l += 1
            window.add(s[r])
            res = max(res, r - l + 1)
        
        return res
            