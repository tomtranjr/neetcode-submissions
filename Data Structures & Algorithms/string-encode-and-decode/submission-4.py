class Solution:
    def encode(self, strs: List[str]) -> str:
        # create an empty list, res
        # for each string in strs:
        # append length + delim char # + string itself
        # then return a joined string from the elements in res
        res = []
        for char in strs:
            res.append(str(len(char)))
            res.append("#")
            res.append(char)
        return "".join(char for char in res)

    def decode(self, s: str) -> List[str]:
        # init empty list res
        # we have a list of strings
        # using example 1: s = "5#Hello5#World"
        # init two pointers, L and R
        # scan string for length
        # update L to idx after delim and R to idx + length
        # extract that and append to res
        # then update L pointer to find the length of next string, repeat until end of string
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        return res
            
