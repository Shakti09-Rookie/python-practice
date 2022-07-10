# https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s=="":
            return True
        s1=''
        for i in s:
            if i.isalnum():
                s1+=i
        if s1.lower()==s1.lower()[::-1]:
            return True
        else:
            return False