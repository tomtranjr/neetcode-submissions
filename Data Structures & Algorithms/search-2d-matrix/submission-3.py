class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        search_space = matrix[0]
        for i in range(1, len(matrix)):
            for j in range(len(matrix[i])):
                search_space.append(matrix[i][j])

        l, r = 0, len(search_space) - 1
        while l <= r:
            mid = l + (r-l)//2
            if search_space[mid] < target:
                l = mid + 1
            elif search_space[mid] > target:
                r = mid - 1
            else:
                return True
        return False