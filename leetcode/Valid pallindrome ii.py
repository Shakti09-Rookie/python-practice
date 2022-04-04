# daily challenge 02-04-2022
# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

class Solution:            
    def validPalindrome(self, s: str) -> bool:
        end = len(s) -1
        start = 0
        flag = 0
        def ispal(s, start, end):
            if(start == end):
                return True
            
            while start< end:
                if s[start] != s[end]:
                    return False
                start+=1
                end-=1
            return True
        
        
        while start< end:
            if s[start] != s[end]:
                return ispal(s, start+1, end) or ispal(s,start, end-1)
            start+=1
            end-=1
        return True
# one at a time
a = ["aba",
"abca",
"abc",
"cbbcc"]
obj1 = Solution().validPalindrome(a)