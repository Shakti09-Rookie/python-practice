# Daily Challenge 11-05-2022
# https://leetcode.com/problems/count-sorted-vowel-strings/

class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [1] * 5
                                
        for _ in range(1, n):
            for i in range(1, 5):                    
                dp[i] = dp[i] + dp[i-1]
        
        return sum(dp)