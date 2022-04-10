# Daily Challenge 10-04-2022
# https://leetcode.com/problems/baseball-game/
from typing import List

class Solution:
    def calPoints(self, ops: List[str]) -> int:
        i =0
        while i < len(ops):
            if ops[i] == "+":
                ops[i]= int(ops[i-2])+int(ops[i-1])
            elif ops[i] == "D":
                ops[i] = 2*int(ops[i-1])
            elif ops[i] == "C":
                ops.pop(i)
                ops.pop(i-1)
                i=i-2
            else:
                ops[i] = int(ops[i])
            i+=1
        return sum(ops)

ops = ["5","2","C","D","+"]
obj1 = Solution().calPoints(ops)