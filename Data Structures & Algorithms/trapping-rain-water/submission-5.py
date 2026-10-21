class Solution:
    def trap(self, height: List[int]) -> int:
        # two pointer
        l, r = 0, len(height) - 1

        res = 0

        leftWall, rightWall = height[l], height[r] # 0, 1

        while l < r:
            if leftWall >= rightWall:
                r -= 1
                rightWall = max(rightWall, height[r])
                res += rightWall - height[r]
            else:
                l += 1
                leftWall = max(leftWall, height[l])
                res += leftWall - height[l]
        
        return res