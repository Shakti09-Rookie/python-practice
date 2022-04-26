# Daily Challenge 26-04-2022
# https://leetcode.com/problems/min-cost-to-connect-all-points/

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        l = list()
        heapq.heappush(l,[0, points[0][0], points[0][1]])
        for i in range(1,len(points)):
            heapq.heappush(l,[float('inf'), points[i][0],points[i][1]])
            
        summ = 0
        
        while l :
            val,x,y = heapq.heappop(l)
            summ+= val
            for i in range(len(l)):
                tt,xx,yy = l[i]
                l[i][0] = min(l[i][0], abs(x-xx) + abs(y-yy))
            heapq.heapify(l)
        return summ
