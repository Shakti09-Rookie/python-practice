# Daily Challenge 25-08-2022
# https://leetcode.com/problems/ransom-note/

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom = sorted(list(ransomNote))
        mag = sorted(list(magazine))
        
        for character in mag:
            if ransom and character == ransom[0]:
                ransom.pop(0)
                
        if ransom:
            return False
        else:
            return True