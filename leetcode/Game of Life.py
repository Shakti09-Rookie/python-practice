# Daily Challenge 12-04-2022
# https://leetcode.com/problems/game-of-life/

from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        def check(i,j,n,m):
            if i>=0 and i<n and j>=0 and j<m:
                return True
            else:
                return False
        n=len(board)
        m=len(board[0])
        count=0
        d=[]
        for i in range(n):
            a=[]
            for j in range(m):
                a.append(board[i][j])
            d.append(a)
    
        for i in range(n):
            for j in range(m):
                if check(i-1,j-1,n,m):
                    if d[i-1][j-1]==1:
                        count+=1
                if check(i-1,j,n,m):
                    if d[i-1][j]==1:
                        count+=1
                if check(i-1,j+1,n,m):
                    if d[i-1][j+1]==1:
                        count+=1
                if check(i,j-1,n,m):
                    if d[i][j-1]==1:
                        count+=1
                if check(i,j+1,n,m):
                    if d[i][j+1]==1:
                        count+=1
                if check(i+1,j-1,n,m):
                    if d[i+1][j-1]==1:
                        count+=1
                if check(i+1,j,n,m):
                    if d[i+1][j]==1:
                        count+=1
                if check(i+1,j+1,n,m):
                    if d[i+1][j+1]==1:
                        count+=1
                if count<2 or count>3:
                    board[i][j]=0
                elif count==3:
                    board[i][j]=1
                count=0
        return board

board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
obj1 = Solution().gameOfLife(board)
print(obj1)