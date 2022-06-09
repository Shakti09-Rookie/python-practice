# Daily Challenge 08-06-2022
# https://leetcode.com/problems/remove-palindromic-subsequences/

class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if not s:
            return 0
        if s == s[::-1]:
            return 1
        else:
            return 2