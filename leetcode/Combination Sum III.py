# Daily Challenge 10-05-2022
# https://leetcode.com/problems/combination-sum-iii/

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        output = []
        def dfs(ans, num, summ):
            if len(ans) == k and summ == n:
                output.append(ans)
                return
            
            for i in range(num, 10):
                if summ+i > n: break
                dfs(ans+[i], i+1, summ+i)
                
        dfs([], 1, 0)
        return output