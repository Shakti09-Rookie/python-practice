# Daily Challenge 22-05-2022
# https://leetcode.com/problems/palindromic-substrings/

class Solution:
    def countSubstrings(self, s: str) -> int:
        output = 0
        N = len(s)
        
        for a in range(N):
            i,j = a,a
            while 0<=i<N and 0<=j<N and s[i] == s[j]:
                output+=1
                i-=1
                j+=1
            i,j = a, a+1
            while 0<=i<N and 0<=j<N and s[i]==s[j]:
                output+=1
                i-=1
                j+=1
        return output