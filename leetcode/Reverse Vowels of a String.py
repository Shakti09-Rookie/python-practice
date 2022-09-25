# https://leetcode.com/problems/reverse-vowels-of-a-string/

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U" ]
        new = []
        output = ""
        for i in s:
            if i in vowels:
                new.append(i)
        for i in s:
            if i not in vowels:
                output+=i
            else:
                output+=new[-1]
                new.pop()
        return output