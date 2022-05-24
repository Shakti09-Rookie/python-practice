# Daily Challenge 24-05-2022
# https://leetcode.com/problems/longest-valid-parentheses/

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        cur_length = 0
        maxl = 0
        for e in s:
            if e == ")":
                if stack:
                    cur_length += stack.pop() + 2
                    maxl = max(maxl, cur_length)
                else:
                    cur_length = 0
            elif e == "(":
                stack.append(cur_length)
                cur_length = 0
        return maxl