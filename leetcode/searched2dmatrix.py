"""
#daily challenge 30-03-2022
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. 
This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
"""

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nr = len(matrix)
        nc = len(matrix[0])
        for i in range(nr):
            for j in range(nc):
                if matrix[i][j] == target:
                    return True
        return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
obj1  = Solution().searchMatrix(matrix, 3)
print(obj1)