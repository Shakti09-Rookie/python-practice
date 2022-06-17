# Daily Challenge 16-06-2022
# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = 0
        ss = ''
    
        for i in range(len(s)):
            l,r = i,i
            while (l>=0) and (r<len(s)) and s[l]==s[r]:
                if (r-l+1)>res:
                    res= (r-l+1)
                    ss = s[l:r+1]
                l-=1
                r+=1

            l,r = i,i+1
            while (l>=0) and (r<len(s)) and s[l]==s[r]:
                if (r-l+1)>res:
                    res= (r-l+1)
                    ss = s[l:r+1]
                l-=1
                r+=1

        return ss