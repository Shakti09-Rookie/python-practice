# Daily Challenge 11-04-2022
# https://leetcode.com/problems/shift-2d-grid/

from typing import List

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])
        if m==1 and n==1:
            return grid
    
        rt = k // m
        for i in range(rt):
            grid = [ grid[n-1] ] + grid[:n-1]
    
        k = k % m
        if k == 0:
            return grid
        arr = [ grid[i][j] for i in range(n) for j in range(m)]
        arr = arr[-k:] + arr[:-k]
        grid = []
        for i in range(n):
            grid.append(arr[m*i:m*(i+1)])
        return grid

grid = [[1,2,3],[4,5,6],[7,8,9]]
k = 1
obj1 = Solution().shiftGrid(grid, k)
print(obj1)

"""
# from leetcode discussions
class Solution(object):
    def shiftGrid(self, grid, k):
        l, m, n, k = [num for row in grid for num in row], len(grid), len(grid[0]), k % (len(grid) * len(grid[0]))  # grid to list
        l = l[-k:] + l[:-k]  # shift k times
        return [l[i * n: i * n + n] for i in range(m)]  # list to grid

check to see more solutions on discussion page.
"""