# Daily Challenge 13-06-2022
# https://leetcode.com/problems/triangle/

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [0] * ( len(triangle) + 1)
        for row in triangle[::-1]:
            for pos, item in enumerate(row):
                dp[pos] = item + min (dp[pos],dp[pos+1])
        return dp[0]
