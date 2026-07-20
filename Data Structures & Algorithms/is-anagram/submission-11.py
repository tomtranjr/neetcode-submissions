class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_hash = {}
        for char in s:
            if char not in s_hash:
                s_hash[char] = 1
            else:
                s_hash[char] += 1
        
        t_hash = Counter(t)

        return s_hash == t_hash