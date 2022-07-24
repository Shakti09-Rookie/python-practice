# Daily Challenge 24-07-2022
# https://leetcode.com/problems/search-a-2d-matrix-ii/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nr = len(matrix)
        nc = len(matrix[0])
        for i in range(nr):
            for j in range(nc):
                if matrix[i][j] == target:
                    return True
        return False