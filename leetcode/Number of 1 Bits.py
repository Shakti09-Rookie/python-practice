# Daily Challenge 26-05-2022
# https://leetcode.com/problems/number-of-1-bits/

class Solution:
    def hammingWeight(self, n: int) -> int:
        wt=0
        for i in range(32):
            if((n & (1<<i)) !=0):
                wt+=1
        return wt