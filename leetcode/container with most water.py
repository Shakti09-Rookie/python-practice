# daily challenge 05-04-2022
# https://leetcode.com/problems/container-with-most-water/
# greedy algorithm

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height) - 1
        mw = 0
        i = 0
        while(i<n):
            mw = max(mw, (n-i)* min(height[i], height[n]))
            if height[i] < height[n]:
                i+=1
            else:
                n-=1
        return mw

obj1 = Solution().maxArea(height)
print(obj1)

# correct but too slow on big test cases
# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         n = len(height)
#         mw = 0
#         for i in range(n):
#             print("height",height[i])
#             print("i ->",i)
#             counter = 0
#             for j in range(i+1,n):
#                 counter+=1
#                 print("counter", counter)
#                 print("j", j)
#                 print("element at j, but from outside->", height[j])
#                 if height[i] * counter > mw and height[i]<= height[j]:
#                     mw = height[i]*counter
#                     print("element at j ->", height[j])
#                     print("mw ", mw)
#                 elif height[j] * counter > mw and height[j]<= height[i]:
#                     mw = height[j]*counter
#         # print(mw)
#         return mw


#  more optimised greedy algorithm by someone else
# class Solution(object):
#     def maxArea(self, height):
#         l, r, area = 0, len(height) - 1, 0
#         while l < r:
#             min_height=min(height[l], height[r])
#             area = max(area, (r - l) * min_height)
#             if height[l] < height[r]:
#                 l+=1
#                 while height[l]<min_height:
#                     l+=1
#             else:
#                 r-=1
#                 while height[r]<min_height:
#                     r-=1			
#         return area