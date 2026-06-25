class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        r = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                # get index where temp is small
                j = stack.pop()
                r[j] = i - j
            stack.append(i)
        
        return r