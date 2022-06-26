# https://leetcode.com/problems/length-of-last-word/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s2 = s.rstrip()
        string_to_list = list(s2.split(" "))
        last_string = string_to_list[-1]
        length = len(last_string)
        return length