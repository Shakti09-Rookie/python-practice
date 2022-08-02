# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        lst = []
        for i in matrix:
            for j in i:
                lst.append(j)
                
        lst.sort()       
        return lst[k-1]