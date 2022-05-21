# Daily Challenge 21-05-2022
# https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[float('inf') for i in range((amount)+1)]
        dp[0] = 0
        
        for i in range(len(dp)):
            for c in coins:
                if i-c>=0:
                    dp[i] = min(dp[i],dp[i-c]+1)
                    
        return -1 if dp[-1] == float('inf') else dp[-1]