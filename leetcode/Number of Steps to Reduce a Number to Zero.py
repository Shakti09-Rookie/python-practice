# Daily Challenge 27-05-2022
# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

class Solution:
    def numberOfSteps(self, num: int) -> int:
        n = 0
        while num>0:
            if num%2==0:
                num = num//2
            else:
                num-=1
            n+=1
        return n