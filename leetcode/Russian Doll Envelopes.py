# Daily Challenge 25-05-2022
# https://leetcode.com/problems/russian-doll-envelopes/

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        env = sorted(envelopes, key = lambda x: (x[0], -x[1]))
        dp =[]
        for w,h in env:
            i = bisect_left(dp, h)
                    
            if i==len(dp):
                dp.append(h)
            else:
                dp[i] = h
                
        return len(dp)