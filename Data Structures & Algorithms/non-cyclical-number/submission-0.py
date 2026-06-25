class Solution:
    def isHappy(self, n: int) -> bool:

        def _sum_square_digits(n: int) -> int:
            sum = 0
            for char in str(n):
                sum += int(char)**2
            return sum

        seen = dict()

        while True:
            n = _sum_square_digits(n)
            if n == 1:
                return True
            if n in seen:
                return False
            seen[n] = 1