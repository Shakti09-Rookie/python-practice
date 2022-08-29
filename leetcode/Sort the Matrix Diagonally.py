# Daily Challenge 28-08-2022(ND)
# https://leetcode.com/problems/sort-the-matrix-diagonally/

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        for i in range(m):
            mat[i] = mat[i][::-1]
        d = defaultdict(list)
        for i in range(m):
            for j in range(n):
                d[i+j].append(mat[i][j])
        for i in d:
            d[i].sort()
        for i in range(m):
            for j in range(n):
                mat[i][j] = d[i+j].pop(0)
        for i in range(m):
            mat[i] = mat[i][::-1]
        return mat