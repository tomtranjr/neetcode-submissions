class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # init
        maxArea = 0
        # track pair: (index, height)
        # more specifically, index this height can start at
        stack = [] 
        
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea