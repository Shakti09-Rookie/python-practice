# Daily Challenge 13-04-2022
# https://leetcode.com/problems/spiral-matrix-ii/

from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat= [[0] * n for _ in range(n)]
        top, left, down, right = 0, 0, n, n
        dir = 0
        count = 1
        while(top <= down and left <= right):
            if(dir == 0):
                for i in range(left, right):
                    mat[top][i] = count
                    count+=1
                top+=1
            elif(dir == 1):
                for i in range(top , down ):
                    mat[i][right-1] = count
                    count+=1
                right-=1
            elif(dir == 2):
                for i in reversed(range(left, right)):
                    print(left, right, down)
                    mat[down-1][i] = count
                    count+=1
                down-=1
            elif(dir == 3):
                for i in reversed(range(top, down)):
                    mat[i][left] = count
                    count+=1
                left+=1
            dir = (dir+1)%4
        return mat


n = 3        
obj1 = Solution().generateMatrix(n)
print(obj1)