class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tracker = dict()

        for word in strs:
            key = "".join(sorted(word))
            if key in tracker:
                tracker[key].append(word)
            else:
                tracker[key] = [word]
        
        # output = []
        # for value in tracker.values:
        #     output.append(value)
        # return output
        return list(tracker.values())