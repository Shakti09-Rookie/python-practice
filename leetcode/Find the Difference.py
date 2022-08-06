# https://leetcode.com/problems/find-the-difference/

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ss = sorted(s)
        ts = sorted(t)
        for i in range(len(s)):
            if ss[i] != ts[i]:
                return ts[i]
        return ts[-1]