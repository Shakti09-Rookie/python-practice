# Daily Challenge 01-05-2022
# https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        a,b = [], []
        for i in s:
            if i == "#":
                if a:
                    a.pop()
            else:
                a.append(i)
        for j in t:
            if j == "#":
                if b:
                    b.pop()
            else:
                b.append(j)
        if a == b:
            return True
        else:
            return False