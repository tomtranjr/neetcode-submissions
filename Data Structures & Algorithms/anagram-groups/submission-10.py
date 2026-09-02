class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = defaultdict(list)

        for string in strs:
            key = "".join(sorted(string))
            store[key].append(string)
        
        return list(store.values())