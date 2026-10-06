class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for c in strs:
            key = "".join(sorted(c))
            res[key].append(c)
        
        return [res for res in res.values()]
