# https://leetcode.com/problems/shuffle-string/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        d={}
        for i in range(len(indices)):
            d[indices[i]]=s[i]

        ans=""
        for j in range(len(d)):
            ans=ans+d[j]
        return ans