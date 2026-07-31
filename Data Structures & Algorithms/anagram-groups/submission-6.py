class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tracker = defaultdict(list)

        for word in strs:
            key = "".join(sorted(word))
            tracker[key].append(word)
        
        return list(tracker.values())