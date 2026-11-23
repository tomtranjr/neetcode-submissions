class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # join all digits into a string
        # convert string to int + 1
        # create list from int
        # return list
        tmp = "".join([str(x) for x in digits])
        tmp = int(tmp) + 1
        res = [x for x in str(tmp)]
        return res