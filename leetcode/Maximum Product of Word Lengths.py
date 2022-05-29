# Daily Challenge 29-05-2022
# https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        lookup = defaultdict(set)
        for w in words:
            lookup[w] = set(w)
            
        def dont_share(s,t):
            if lookup[s]& lookup[t]:
                return False
            return True
        
        mx =0
        for i in words:
            for j in words:
                if dont_share(i,j):
                    mx = max(mx, len(i) * len(j))
                    
        return mx