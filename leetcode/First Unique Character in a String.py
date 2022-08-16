# Daily Challenge 16-08-2022
# https://leetcode.com/problems/first-unique-character-in-a-string/

class Solution:
    def firstUniqChar(self, s: str) -> int:
        duplicate = Counter(s)
        for i, c in enumerate(s):
            if duplicate[c] == 1:
                return i
        return -1