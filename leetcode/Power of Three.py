# Daily Challenge 24-08-2022
# https://leetcode.com/problems/power-of-three/

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        mx = 3**19
        return n>0 and mx%n==0