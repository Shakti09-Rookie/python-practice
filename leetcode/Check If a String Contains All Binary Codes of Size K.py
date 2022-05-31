# Daily Challenge 31-05-2022
# https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        sub = 2**k
        N = len(s)
        sset = set([s[i:i+k] for i in range(N+1-k)])
        
        return sub == len(sset)