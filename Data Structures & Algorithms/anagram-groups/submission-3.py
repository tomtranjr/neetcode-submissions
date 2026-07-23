class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tracker = defaultdict(list) # value are type list

        for word in strs:
            key = "".join(sorted(word)) # sorted(word) creates sorted list
            tracker[key].append(word)
        
        return list(tracker.values())