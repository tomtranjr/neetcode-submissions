class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # take array convert to str to int
        # int + 1
        # take int to str to array
        # return array
        tmp = "".join([str(x) for x in digits])
        tmp = int(tmp) + 1
        res = [x for x in str(tmp)]
        return res